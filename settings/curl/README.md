<h2 align='center'> File curl.py </h2>

### 📋 Информация о получении cURL

В файле curl.py предоставленны следующие константы настроек:

    COOKIES = {
        'gdpr': 'YOUR ',
        '_ym_uid': 'YOUR _ym_uid',
        '_yasc': 'YOUR _yasc',
        'yandex_login': 'YOUR yandex_login',
        'i': 'YOUR i',
        'yandexuid': 'YOUR yandexuid',
        'location': 'YOUR location',
        'crookie': 'YOUR crookie',
        'cmtchd': 'YOUR cmtchd',
        'coockoos': 'YOUR coockoos',
        'yuidss': 'YOUR yuidss',
        '_csrf': 'YOUR _csrf',
        'ya_sess_id': 'YOUR ya_sess_id',
        'ys': 'YOUR ys',
        'mda2_beacon': 'YOUR mda2_beacon',
        'sso_status': 'YOUR sso_status',
        'desktop_session_key': 'YOUR desktop_session_key',
        'desktop_session_key.sig': 'YOUR desktop_session_key.sig',
        '_ym_isad': 'YOUR _ym_isad',
        'yp': 'YOUR yp',
        'ymex': 'YOUR ymex',
        'kdetect': 'YOUR kdetect',
        'PHPSESSID': 'YOUR PHPSESSID',
        'user_country': 'YOUR user_country',
        'yandex_gid': 'YOUR yandex_gid',
        'tc': 'YOUR tc',
        'uid': 'YOUR uid',
        '_ym_d': 'YOUR _ym_d',
    }
    
    HEADERS = {
        'authority': 'www.kinopoisk.ru',
        'accept': 'YOUR accept',
        'accept-language': 'YOUR accept-language',
        'cache-control': 'YOUR cache-control',
        'referer': 'https://www.kinopoisk.ru/',
        'sec-ch-ua': 'YOUR sec-ch-ua',
        'sec-ch-ua-mobile': 'YOUR sec-ch-ua-mobile',
        'sec-ch-ua-platform': 'YOUR sec-ch-ua-platform',
        'sec-fetch-dest': 'YOUR sec-fetch-dest',
        'sec-fetch-mode': 'YOUR sec-fetch-mode',
        'sec-fetch-site': 'YOUR sec-fetch-site',
        'sec-fetch-user': 'YOUR sec-fetch-user',
        'upgrade-insecure-requests': 'YOUR upgrade-insecure-requests',
        'user-agent': fake_agent,
    }
    
    PARAMS = {
        'sort': 'rating',
        'b': 'films',
    }
    
    HEADERS_MOVIE = {
        'authority': 'www.kinopoisk.ru',
        'accept': 'YOUR accept',
        'accept-language': 'YOUR accept-language',
        'cache-control': 'YOUR cache-control',
        'sec-ch-ua': 'YOUR sec-ch-ua',
        'sec-ch-ua-mobile': 'YOUR sec-ch-ua-mobile',
        'sec-ch-ua-platform': 'YOUR sec-ch-ua-platform',
        'sec-fetch-dest': 'YOUR sec-fetch-dest',
        'sec-fetch-mode': 'YOUR sec-fetch-mode',
        'sec-fetch-site': 'YOUR sec-fetch-site',
        'sec-fetch-user': 'YOUR sec-fetch-user',
        'upgrade-insecure-requests': 'YOUR upgrade-insecure-requests',
        'user-agent': fake_agent,
    }

PARAMS трогать не следует. 

Получение информации происходит при помощи просмотра элементра страницы и 
обработке данных на сайте: https://curlconverter.com/

### 💡 Для настройки COOKIES и HEADERS

1) Переходим на сайт https://www.kinopoisk.ru/
2) Открываем просмотр кода страницы - F12
3) Переходим во вкладку 'Network' и обновляем страницу
4) На `первом месте` загрузится ответ с названием `www.kinopoisk.ru`
5) ПКМ по ячейке с названием выше -> Copy -> Copy as cURL(bash)
6) Переходим на сайт https://curlconverter.com/, вставляем данные и получаем 
ответ с нужными нам константами - `cookies` и `headers`
7) Заменяем данные в `COOKIES` и `HEADERS` на `cookies` и `headers`.

Обратите внимание на `user-agent` в `HEADERS`. Он должен 
остаться равным `fake_agent`!

### 💡 Для настройки HEADERS_MOVIE

1) Переходим по любой ссылке с фильмом(Например: https://www.kinopoisk.ru/film/435/)
2) Повторяем действия из списка выше (С пункта 2 по 5)
3) Переходим на сайт https://curlconverter.com/, вставляем данные и получаем 
ответ с нужной нам константой - `headers`
4) Заменяем данные в `HEADERS` на `headers`.

Обратите внимание на `user-agent` в `HEADERS_MOVIE`. Он должен 
остаться равным `fake_agent`!

*** 
Создатель снимает с себя ответственноть за возможную блокировку IP адреса на стороне kinopoisk. 
***