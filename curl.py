
from fake_useragent import UserAgent
fake_agent = UserAgent().random

COOKIES = {
    'gdpr': '0',
    '_ym_uid': '1677954667513282420',
    '_yasc': 'GhSBToCxO2WMT89FVlhPMBrAUiPyCn7rREwmDTxUQydU/wVhUZRLu4bPBrS/',
    'yandex_login': 'goodmaxmail.ru',
    'i': 'G0osSoelaGdZBlZty/THQkQ9BL8opsNvJnUy6MX6aM8Zl/YobL92DOLYrlHNZIj9pkFOf5i5jvNoFJVA7AOv21b1Yb4=',
    'yandexuid': '6664497391640431753',
    'location': '1',
    'crookie': 'TC8vb/eqmEBgeYDRpnN0jn8IXc59pyGD04yBrkiov+hVEWOTKNtREqx1F1TpHhrVm2BsdUzIGyeCzYLneqmN2qpPVl0=',
    'cmtchd': 'MTY3Nzk1NTgxNDMxOA==',
    'coockoos': '4',
    'yuidss': '6664497391640431753',
    '_csrf': 'PTe6FoL2azqn8RJINMysCxJ1',
    'ya_sess_id': '3:1678204283.5.0.1640459896446:sHDeTQ:20.1.2:1|371560707.6724698.2.2:6724698|30:10214337.149306.52EYja3TR9nJWNUlcis0khy6Wiw',
    'ys': 'udn.cDrQkNC90L7QvdC40LzQvdC%2B#c_chck.859296887',
    'mda2_beacon': '1678204283638',
    'sso_status': 'sso.passport.yandex.ru:synchronized',
    'desktop_session_key': '302fd8a734d0023a8fef7a648a086f0484b4dbffcc9eaa7e92772720d094b1378363d5a5bb3cb9a2a53f335134118ca2380ab04d5085b9a5487742eb3794abc9cb1e39ee89ce0f15e8d6081d35757bd90ea627f09e748d18f9c1a444e5e329fc',
    'desktop_session_key.sig': 'WY-N1shPdi6m5AsZfA9jwfYjzO8',
    '_ym_isad': '1',
    'yp': '1678290686.yu.6664497391640431753',
    'ymex': '1680796286.oyu.6664497391640431753',
    'kdetect': '1',
    'PHPSESSID': 'a96952db8b9ef0c5f9202d5b6ff0be74',
    'user_country': 'ru',
    'yandex_gid': '56',
    'tc': '454',
    'uid': '35404772',
    '_ym_d': '1678207877',
}

HEADERS = {
    'authority': 'www.kinopoisk.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://www.kinopoisk.ru/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake_agent,
}

PARAMS = {
    'sort': 'rating',
    'b': 'films',
}

HEADERS_MOVIE = {
    'authority': 'www.kinopoisk.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': fake_agent,
}
