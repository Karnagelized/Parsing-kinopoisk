
from fake_useragent import UserAgent
fake_agent = UserAgent().random

"""
Beforehand, you should take cURL from the main kinopoisk site for COOKIES, HEADERS!
Beforehand, you should take cURL from the movie site on the kinopoisk for HEADERS_MOVIE!

You can find how to find cURL and insert it for the parser to work in the project repository
in the settings/curl folder.

Below is an example of data:
"""

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
