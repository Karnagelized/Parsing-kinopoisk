<h2 align='center'> File config.py </h2>

### 📋 Основная информация о Proxy
В данном парсере используется `proxy` для большей безопасности пользователя 
в случае блокировки IP сервером kinopoisk.

Происходит это из-за того что отправляя запрос сервер проверяет нас 
на 'подделку'. В худшем случае происходит `блокировка` IP на `24` часа.

В файле confing.py предоставлены следующие константы:

    IP = 'YOUR IP'
    
    PORT = 'YOUR PORT'
    
    LOGIN = 'YOUR LOGIN'
    
    PASSWORD = 'YOUR PASSWORD'
    
    PROXIES = {
        #"http": f"http://{LOGIN}:{PASSWORD}@{IP}:{PORT}",
    }

При подключении используется `http` запрос, но по желанию можете добавить и другие.

Если вы оставите PROXIES с закомментированной строкой, то будет использоваться Ваш
IP адрес для запросов на сайт.

### 📋 Информация про настройку

В файле confing.py предоставлены следующие константы настроек:

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

* YEARS - Отвечает за выборку лет фильмов.
* USER_PAGINATION - Личная ваша пагинация по выборке фильмов. От её настройки 
зависит сколько страниц с фильмами будет просмотрено (Если страниц меньше чем 
Ваша настройка пагинации то перебор будет по полученным данным)
* GLOBAL_URL и COUNTRY - ссылка и название страны. 

💡 Ссылка - берётся при переходе на страницу: https://www.kinopoisk.ru/lists/categories/movies/9/

Требуется выбрать страну и вставить ссылку в константу GLOBAL_URL по следующему шаблону:
...kinopoisk.ru/lists/movies/country--(число))/(заменить на 'year--')

`НА ЭТУ ЖЕ ПОЗИЦИЮ` вставить название страны в константу COUNTRY.

*** 
Создатель снимает с себя ответственность за возможную блокировку IP адреса на стороне kinopoisk.ru. 
***