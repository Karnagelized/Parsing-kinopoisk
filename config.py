
# Proxy
"""
!!! Use a proxy so that you are not blocked from the server side. !!!

See the installation instructions in the project repository in the settings/proxy folder.
"""

IP = 'YOUR IP'

PORT = 'YOUR PORT'

LOGIN = 'YOUR LOGIN'

PASSWORD = 'YOUR PASSWORD'

PROXIES = {
    #"http": f"http://{LOGIN}:{PASSWORD}@{IP}:{PORT}",
}

# Sample for number of years
YEARS = range(2022, 2023)

# Number of pages for the withdrawal of films
USER_PAGINATION = 1

# Link to your country page with the specified year
GLOBAL_URL = [
    'https://www.kinopoisk.ru/lists/movies/country--1/year--',
]

# Country
COUNTRY = [
    'США',
]
