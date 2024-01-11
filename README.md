# telegram-parser-v2.0. Парсер и инвайтер чатов Телеграмм. (Telethon) 

![Watermark](https://github.com/Keqy/telegram-parser-v1.0/assets/96333229/bb1e06e4-83a5-4302-83b6-3d530fcaa14f)

# Обновления
## v2.0
* __.session - файлы теперь можно использовать для авторизации. Достаточно закинуть их в директорию!__
* __добавлен парсинг юзер-id.__
* __функция включения/выключения парсинга юзернеймов и юзер-id. (в настройках)__
* __конвертор номеров телефонов в .session__
  


## 1. Подготовка к запуску.
Перед началов нужно узнать свой API_ID и API_HASH токены. Переходим на сайт: https://my.telegram.org/apps и авторизуемся. Выбераем пункт __API Development Tools__

![12591615102022_5c20dcbcfbab07ab6c2df7e27444d5ac2afca569](https://github.com/Keqy/telegram-parser-v1.0/assets/96333229/75080769-1aa6-4cbc-ab75-cd0a1e04ec09)

В следующем окне заполняем поля: App title и Short name. Выбираем desktop.

![gfbauf](https://github.com/Keqy/telegram-parser-v1.0/assets/96333229/963ca90a-b9f7-4f94-bc95-a87742742239)

Нажимаем Create Application и из возникнувшего окна сохраняем себе API_ID и API_HASH. 
__API_ID и API_HASH подходят к любым аккаунтам. Можно использовать API_ID и API_HASH стороннего аккаунта__
## 2. Сборка проекта.
__Windows__
* Скачиваем python 3.12 по ссылке https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe
* __При установке обязательно ставьте галочку у Add to PATH__
  ![hgai](https://github.com/Keqy/telegram-parser-v1.0/assets/96333229/046ed050-5a00-4c94-8758-6de165e81ca3)
* Открываем командную строку(Клавиша "win" + клавиша "R" и команда ```cmd```)
* Командой ```cd``` ведём к директории парсера. Пример: ```cd C:Users/Keqy/programs/repos/telegram-parser-v2.0```
* Создаёте виртуальное окружение ```py -m venv venv```, активируете его ```.\venv\Scripts\Activate```
* Устанавливаете telethon ```pip install telethon```

__Linux/MacOS__
* Открываем терминал, обновляем пакеты. ```sudo apt update```
* Устанавливаем python и git. ```sudo apt install python3 python3-pip git -y```
* Скачиваем репозиторий. ```git clone https://github.com/Keqy/telegram-parser-v2.0/```
* ```cd``` в директорию парсера.
* Создаём виртуальное окружение ```py -m venv venv```, активируете его ```.\venv\bin\Activate```


## 3. Использование.
После первого запуска откроются настройки парсера.

![image](https://github.com/Keqy/telegram-parser-v2.0/assets/96333229/b465cb54-843f-4fe2-94ed-c5e68836a923)

Введите ваш API_ID. __он содержит только цифры. Без пробелов__
Введите ваш API_HASH. __API_HASH содержит только цифры и буквы латинского алфавита. Без пробелов__
Здесь же в пункте 3 и 4 можно вкл/выкл функцию парсинга юзернеймов/юзер-id. По умолчанию парсится и то и другое.

__КОНВЕРТОР__

Конвертор находится в настройках в пункте ```Добавить аккаунт юзербота```. В конвертор поступает номер телефона аккаунта телеграмм. В директории проекта создаётся .session файл для быстрой авторизации юзербота. Свои .session файлы так же можно добавить в корневую папку и парсить/инвайтить через них.

![image](https://github.com/Keqy/telegram-parser-v2.0/assets/96333229/9fc11349-ddf8-441e-a386-a301847a5942)

__конвертор не работает если API_ID или API_HASH не действительны или введены с ошибками__
__для каждого нового аккаунта __НЕ__ требуется новый API_ID и API_HASH__

Настройки хранятся в ```options.txt``` в директории проекта.
После настройки введите латинскую ```e```. В парсере она используется для выхода.
После выхода из настроек откроется основное меню.

![image](https://github.com/Keqy/telegram-parser-v2.0/assets/96333229/8a764eab-22db-429e-a900-514a78c3d46f)

### Парсинг
В окне парсинга выбирайте аккаунт который состоит в группах, которые нужно спарсить.

![image](https://github.com/Keqy/telegram-parser-v2.0/assets/96333229/00a72f59-f2d3-496b-80d8-63f9507f7a1b)

![image](https://github.com/Keqy/telegram-parser-v2.0/assets/96333229/56a17b94-fb7b-4e16-84ad-9ebc9f7b131a)

__Иногда на этом моменте может вылетать ошибка библиотеки. В этом случае надо перезапустить программу__

Спаршенные юзернеймы и юзер-id будут лежать в директории в файлах ```usernames.txt``` и ```userids```.

### Инвайтинг
В окне инвайтинга выберите аккаунт который состоит в группе для инвайтинга. Затем введите имя группы.


__Пишите мне в телеграмм ```@DonMinionAmerimaChesburger```___
[Watermark](https://github.com/Keqy/telegram-parser-v1.0/assets/96333229/526fb03e-0921-4baf-8e8d-6f0cee8a9002)

