
import requests
import re
import json
import pandas as pd
from bs4 import BeautifulSoup

from config import PROXIES, GLOBAL_URL, USER_PAGINATION, YEARS, COUNTRY
from curl import COOKIES, HEADERS, PARAMS, HEADERS_MOVIE
from functions import timingDecorator

# Movie data lists
link = []
name = []
annum = []
country = []
director = []
rating = []
budget = []
fees = []
genre = []
age = []
duration = []

# Parsing movie menu data
def get_menu_data(menu_list):
    temp_director = 'Отсутствует'
    temp_budget = '0'
    temp_fees = '0'
    temp_genre = 'Отсутствует'
    temp_age = 'Отсутствует'
    temp_duration = 'Отсутствует'

    for category in menu_list:
        # Finding a Director
        if category.next_element.text == 'Режиссер':
            try:
                temp_director = ', '.join([_.text for _ in category.find_all('a', attrs={'data-tid': '603f73a4'})])
            except Exception as e:
                print(f'Director data Error: {e}')

        # Search a Budget
        if category.next_element.text == 'Бюджет':
            try:
                temp_budget = ', '.join([_.text for _ in category.find('a')])
            except Exception as e:
                print(f'Budget data Error: {e}')

        # Search Fees in the world
        if category.next_element.text == 'Сборы в мире':
            try:
                total_fees = ''.join(re.findall('\S+', category.find('a').text))
                temp_fees = total_fees[total_fees.find('=') + 1:]
            except Exception as e:
                print(f'Fees data Error: {e}')

        # Search Genre
        if category.next_element.text == 'Жанр':
            try:
                temp_genre = ', '.join([_.text for _ in category.find_all('a', attrs={'data-tid': '603f73a4'})])
            except Exception as e:
                print(f'Genre data Error: {e}')

        # Search Age
        if category.next_element.text == 'Возраст':
            try:
                temp_age = category.find('span', attrs={'data-tid': '5c1ffa33'}).text
            except Exception as e:
                print(f'Age data Error: {e}')

        # Search Duration
        if category.next_element.text == 'Время':
            try:
                if category.find('div', attrs={'data-tid': 'e1e37c21'}):
                    temp_duration = category.find_all('div', attrs={'data-tid': 'e1e37c21'})[-1].next_element.text
            except Exception as e:
                print(f'Duration data Error: {e}')

    # Adding information
    director.append(temp_director)
    budget.append(temp_budget)
    fees.append(temp_fees)
    genre.append(temp_genre)
    age.append(temp_age)
    duration.append(temp_duration)

@timingDecorator
def main():
    for url_item, url in enumerate(GLOBAL_URL):
        for year in YEARS:
            # Rated-only film processing
            available_rating = True
            global_link = f'{url}{year}/'

            # Processing the main page
            response = requests.get(global_link, params=PARAMS, cookies=COOKIES, headers=HEADERS, proxies=PROXIES)
            soup = BeautifulSoup(response.text, features='lxml')
            pagination = int(soup.find_all('a', attrs={'data-tid': "d4e8d214"})[-2].text)

            # Redefining pagination in case of its minority on the site
            if pagination > USER_PAGINATION:
                pagination = USER_PAGINATION

            # Loop through all pages by pagination
            for page in range(1, pagination + 1):
                page_response = requests.get(f'{global_link}?page={page}', params=PARAMS, cookies=COOKIES, headers=HEADERS, proxies=PROXIES)

                if page_response.status_code == 200:
                    page_soup = BeautifulSoup(page_response.text, features='lxml')
                    movies = page_soup.find_all('a', attrs={'data-tid': '23a2a59'})

                    # Early exit from cycles (No more rated movies)
                    if available_rating == False:
                        print(f'\nIn {year} films are over. Now parse next year.')
                        break

                    print(f'\nParsing page {global_link}?page={page}\n')

                    # Loop through all the movies on the page
                    for item, movie in enumerate(movies):
                        href = f"https://www.kinopoisk.ru{movie.get('href')}"

                        print(f'Parsing movie №{item + 1}: {href}')

                        movie_response = requests.get(href, cookies=COOKIES, headers=HEADERS_MOVIE, proxies=PROXIES)
                        movie_soup = BeautifulSoup(movie_response.text, features='lxml')

                        if movie_response.status_code == 200:
                            # Adding a rating
                            try:
                                if movie_soup.find('span', attrs={'data-tid': '939058a8'}).text != '–':
                                    rating.append(movie_soup.find('span', attrs={'data-tid': '939058a8'}).text)
                                else:
                                    available_rating = False
                                    break
                            except Exception as e:
                                print(f'Rating data Error: {e}')
                                continue

                            # Add a year
                            annum.append(str(year))

                            # Adding a movie country
                            country.append(COUNTRY[url_item])

                            # Add a link to the movie
                            link.append(href)

                            # Reading the movie menu
                            menu = movie_soup.find_all('div', attrs={'data-tid': '7cda04a5'})

                            # Adding a name
                            try:
                                name.append(movie_soup.find('span', attrs={'data-tid': '75209b22'}).text)
                            except Exception as e:
                                print(f'Name data Error: {e}')
                                name.append('Отсутствует')

                            # Adding data from the menu
                            get_menu_data(menu)
                        else:
                            print(f'Error check film: {href}')
                else:
                    print(f'{GLOBAL_URL}?page={page}')

    # Converting data to a dictionary for further conversion to xlsx
    data = {
        'Links': link,
        'Name': name,
        'Director': director,
        'Year': annum,
        'Rating': rating,
        'Country': country,
        'Budget': budget,
        'Fees_in_world': fees,
        'Genre': genre,
        'Age': age,
        'Duration': duration,
    }

    # Log
    with open(f'Films_log.json', 'w+', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=3)

    # Convert and save to xlsx
    try:
        table = pd.DataFrame(data)
        table.to_excel(f'./Films.xlsx')
    except Exception as e:
        print(f'Error saving data in xlsx: {e}')

if __name__ == '__main__':
    main()
