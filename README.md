# smm_planner
Это командный учебный проект, выданный на [Девман](https://dvmn.org/). Цель проекта научиться работать в команде в условиях неадекватных пожеланиях Заказчика.

# Пожелания Заказчика
Бизнесмен Виталий ведет каналы  соцсетях о своем производстве ножей НКВД. Чтобы не отдавать каждый месяц деньги и доступы создателям SMMplanner, он решил заплатить один раз команде разработки – то есть вам. Виталий хочет просто нажимать несколько кнопок – и чтобы пост сам появлялся в нужных соцсетях. 
Разумеется, и здесь не без чудачеств: Виталий любит работать в Google Таблицах, поэтому и программа должна быть завязана на них.
Идея такая: Виталий вводит в Таблицу ссылку на Google Документ с текстом публикации, её дату и соцсеть. А дальше пост сам появляется в нужное время в нужном месте.
Пока что это Вконтакте, Telegram-канал и конечно же Одноклассниках.  

# Для корректной работы скрипта необходимо провести подготовительные работы и быть зарегистрированным пользователем вышеуказанных социальных сетей. 

# ОДНОКЛАССНИКИ
## Получить ключи для Одноклассников по [инструкции](https://apiok.ru/dev/app/create) настройки как на скрине ниже (опционально лучше не ставить)

<img width="950" alt="image" src="https://user-images.githubusercontent.com/55636018/225688509-eab4e7ea-bdd3-4331-927f-49aaedfb65c5.png">


## Пример файла .env 
## часть для Одноклассников

```
OK_ACCESS_TOKEN='tkn1MmVVCFvkuX5fnf9zLFd6RcjsFfv4dt6dhrvxBCe00I7ZO1ZkjK'
OK_APPLICATION_ID='5120823570'
OK_APPLICATION_KEY='CDFENQKGHBABABA'
OK_SECRET_KEY='b5631c1b73dfe9e933f568df8d2a30'
OK_ALBUM='948038190217'
```
OK_ALBUM берется из командной строки после создания нужного Альбома

<img width="408" alt="image" src="https://user-images.githubusercontent.com/55636018/225689782-f46ddfe9-9829-4028-b24b-cae74c35b749.png">

## часть для ВКонтакте
```
VK_GROUP_ID=210000081
VK_ACCESS_TOKEN=vk1.a.veaau-KojaaaXMByg.....EYwgWHlxlj....
```
VK_GROUP_ID берется из адресной строки браузера после создания сообщества

https://vk.com/club **210000081**


VK_ACCESS_TOKEN - получается путем запроса через адресную строку браузера

Инструкция - https://dev.vk.com/api/access-token/getting-started

Метод получения ключа - ``Implicit flow`` для получения ключа доступа пользователя

Пример: запрос
````
https://oauth.vk.com/authorize?client_id=ID_ПРИЛОЖЕНИЯ_ВК&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=photos,wall,offline&response_type=token&v=5.131
````
ID_ПРИЛОЖЕНИЯ_ВК - получаем путем создвания приложения в ВК. 
https://dev.vk.com/ - Мои приложения - Создать приложение - Standalone-приложение

ответ - ключ доступа
````
https://oauth.vk.com/blank.html#access_token=vk1.a.veaau-KojaaaXMByg.....EYwgWHlxlj....&expires_in=0&user_id=2302407
````

.



Если в сообщение не было картинки, то оно выводится ввиде картинки

<img width="620" alt="image" src="https://user-images.githubusercontent.com/55636018/225830469-db80672e-1139-4f0b-9f35-cb844c8b5bda.png">


# Требования к окружению
```
Python 3.xx и выше (должен быть уже установлен)
environs==9.5.0
gspread==5.7.2
python-telegram-bot==13.15
requests==2.28.2
gdown==4.6.4
beautifulsoup4==4.11.2
Pillow==9.4.0
ok_api == 1.0.1

```
# Можно установить командой  
``` 
PIP install -r requirements.txt
```

# Для того чтобы запустить скрипт, войдите в директорию со скриптом и запустите команду:
```
  python3 smm_planner

```
# Пример работы скрипта

в Гугл таблице

<img width="1277" alt="image" src="https://user-images.githubusercontent.com/55636018/226176171-11bff0a1-7da6-4510-82f9-625f542831bd.png">

В Одноклассниках

<img width="1259" alt="image" src="https://user-images.githubusercontent.com/55636018/226176290-9e0c5f12-e4f0-40b1-9f14-3e60f4f39719.png">

Во ВКонтакте

![image](https://user-images.githubusercontent.com/55636018/226176487-f4ea6d89-8421-4163-8932-0054ed852f1f.png)

В Телеграм

![image](https://user-images.githubusercontent.com/55636018/226176509-0d641d8f-38be-4c84-991f-f8269e22ad19.png)


# Отказ от ответственности
Авторы проекта не несут никакой ответственности за то, как вы используете этот код или как вы используете сгенерированные с его помощью данные. Этот проект был написана для обучения и других целей не несет. Не используйте данные, сгенерированные с помощью этого кода в незаконных целях.
