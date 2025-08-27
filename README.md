<h2 align='center'> Parsing kinopoisk.ru </h2>

Парсинг сайта kinopoisk.ru для получения данных из 
фильмов по следующим критериям:

* Ссылка
* Название
* Режиссёр
* Год
* Рейтинг
* Страна
* Бюджет
* Сборы в мире
* Жанр
* Возраст
* Длительность

Добавляются только те фильмы, у которых имеется рейтинг.

Вывод данных осуществляется при помощи xlsx. Вам будет сгенерирован файл 
данного типа со всеми данными.

### 📌 Цель проекта
Собрать данные для проведения аналитического отчёта. Изучить работу с 
xlsx при помощи `pandas`. Попробовать методы оптимизации кода - `async`
(Неудачная попытка - сайт блокирует большое кол-во запросов).

### 🐢 Время выполнения
Код основан на переборе каждого фильма на каждой страницы каждого года. Оптимизацию 
основана на факте сортировки по рейтингу на сайте kinopoisk.ru, а именно:

* Если перебором был найден фильм без рейтинга, то последующие фильмы тоже будут без рейтинга.

В таком случае досрочно завершаем программу и переходим на следующий год или страну.


### 📋 Основные библиотеки
    import beautifulsoup4
    import pandas

### 💡 Установка и запуск
Клонируйте репозиторий, и установите файл requirements.txt
в среде Python >= 3.7.0. В репозитории также приложена актуальная версия .exe приложения. 

    # Clone
    git clone https://github.com/Karnagelized/Parsing-kinopoisk.git
    
    # Moved    
    cd Parsing-kinopoisk
    
    # Install 
    pip install -r requirements.txt

Также следует провести настройку `Proxy` в файле `config.py` и ввести Ваши `cURL` данные 
для работы парсера на kinopoisk.ru в файле `curl.py`.

Вся необходимая информация по настройке парсера находится в репозитории проекта в 
папке `settings`.

### 🔗 Ссылки
<div align="center">
    <a href="https://t.me/masikantonov" style="text-decoration:none;">
        <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>
    </a>
    <a href="https://vk.com/masikantonov" style="text-decoration:none;">
        <img src="https://img.shields.io/badge/VKontakte-2CA5E0?style=for-the-badge&color=0077ff&logo=vk&logoColor=white"/>
    </a>
    <a href="https://pytime.ru" style="text-decoration:none;">
        <img src="https://img.shields.io/badge/PyTime.ru-ffffff?style=for-the-badge&color=0077c2"/>
    </a>
</div>