## Mail Manager – сервис почтовых рассылок

###
Клонируйте репозиторий:
```
git clone https://github.com/bocchitherikka/mail_manager.git
```
Если git не позволяет клонировать репозиторий, вероятно,
у вас нет Git Credential Manager (https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git),
необходимый для клонирования приватных репозиториев по HTTPS.
###
Перейдите в корневой репозиторий:
```
cd mail_manager/mail_manager
```
###
Создайте .env файл с переменными
```
EMAIL_HOST_USER = "some.gmail.address@gmail.com"
EMAIL_HOST_PASSWORD = "app password"
```
Укажите адрес почты Gmail и пароль приложения, который можно создать тут: https://myaccount.google.com/apppasswords. На аккаунте должна быть двухфакторная аутентификация.
###
Запустите докер-контейнеры и настройте их:
```
docker-compose up -d

# Я не знаю почему так, но на этом моменте создается ПАПКА
# вместо бд. Не выключая контейнеры, удалите ее вручную,
# после чего выполняйте следующее:

docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic

# Перезапустите. На всякий случай.

docker-compose down
docker-compose up -d
```
Через логи контейнеров, желательно через удобный GUI Docker Desktop, следите за статусом контейнеров (ОСОБЕННОЕ внимание уделите Celery. Он меня достал в процессе установки) посматривайте, что у вас точно все запустилось.

Если я ничего не упустил, после этого сайт доступен по адресу: http://127.0.0.1:8000
