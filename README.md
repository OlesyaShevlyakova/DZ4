# Бот для отображения цен валют в определенную дату
## Запуск бота
Для запуска нужно добавить secrets.py с переменной TOKEN и значением токена для валидного телеграм бота, полученный от @BotFather

Запуск осуществляется через main.py. Для запуска бота необходимо набрать /start

## Информация о боте
Данный бот позволяет узнавать цену трех валют (доллары, евро и китайские юани) в указанную дату

Информацию берет с сайта Центрального банка РФ (https://cbr.ru/)

## Структура проекта

Состоит из двух файлов:
1) main.py - находится логика телеграм бота
2) currency.py - находится логика парсинга с сайта ЦБ РФ

