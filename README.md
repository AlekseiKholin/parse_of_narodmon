# parse_of_narodmon

Скрипт по получению значения температуры с указанного датчтка

Запрос на сервер:
resp = requests.get('http://narodmon.ru/api/sensorsOnDevice?id='+DEVICE_ID+'&uuid='+UUID+'&api_key='+API_KEY+'&lang=ru').json()

Ответ от сервера:
{"sensors":[{"id":1,"type":0,"value":0,"time":1234567890,"changed":1234567890,"trend":0},{..}]}

- login логин пользователя для авторизации, если он не указан, то возвращается текущий логин для uuid;
- password - пароль авторизации на сайте
- apikey - ключ разработчика, полученный на сайте http://narodmon.ru/
- device id - ID устр-ва из балуна на карте(без первых букв);