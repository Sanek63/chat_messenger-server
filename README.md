# Серверная часть мессенджера на Python

Данный репозиторий является дополнением к [основному репозиторию](https://github.com/Sanek63/chat_messenger-client)
Здесь построена реализация серверной части приложения с помощью Flask фреймворка
и с интеграцией СУБД PostgreSQL.

## Структура репозитория
- **database** - директория базы данных
    - **login.py** - скрипт для подключения к БД
- **test_requests** - директория тестовых запросов
    - **receiver.py** - скрипт для получения сообщений из чата
    - **sender.py** - скрипт для отправки сообщения в чат
- **server.py** - главный исполняемый файл приложения
## Установка

#### Для установки зависимостей проекта необходимо выполнить

```
pip install -r requirements.txt
```

#### Для просмотра списка установленных пакетов

```
pip list
```

## Настройка СУБД

Для настройки СУБД необходимо в скрипте **login.py** (**database** --> *login.py*)
найти конструктор класса. В нем инициализируется подключение к СУБД, где *name* это
имя базы данных. Оно задается пользователем, к какой базе данных использовать соединение.

![image](https://user-images.githubusercontent.com/46131081/95023392-e1992e80-068d-11eb-8c5a-f6de8ee22b6f.png)

Следующая часть конструктора использует процесс подключения к СУБД.
В поле **host** указывается адресс сервера, на котором запущена СУБД,
**database** использует имя базы данных,
**user** и **password** соответственно, имя пользователя и пароль от пользователя СУБД

```
self.conn = psycopg2.connect(
            host="127.0.0.1",
            database=self.dbname,
            user="postgres",
            password="postgres"
        )
```

Как ранее говорилось, имя базы данных инициализируется 
при создание объекта **Login_Database**. Это можно увидеть
в главном исполняемом скрипте **server.py**

![image](https://user-images.githubusercontent.com/46131081/95023632-34271a80-068f-11eb-839d-bd5875011e46.png)

Также, помимо соединения с БД, реализована функция проверки таблицы пользователей.
В случае, если она отсутствует, то система создаст таблицу и внесет туда
пользователя по умолчанию (*admin*, *admin*).

Имя таблицы и создание пользователя по умолчанию также можно изменить.
Для того, чтобы это сделать, необходимо погрузиться в скрипт 
**login.py** (**database** --> *login.py*)

Имя таблицы инициализируется в конструкторе класса

![image](https://user-images.githubusercontent.com/46131081/95023771-ea8aff80-068f-11eb-9c6a-413bd8ce36c9.png)

Имя пользователя и пароль  по умолчанию генерируется при исполнение запроса к БД

![image](https://user-images.githubusercontent.com/46131081/95023814-28882380-0690-11eb-9a8e-0db35577ea8c.png)


## Запуск приложения на глобальном сервере

Для запуска приложения на глобальном сервере, в моем случае,
можно использовать утилиту [ngrok](https://ngrok.com). Утилита
более предназначена для тестирования приложений на глобальном сервере.

Для запуска глобального сервера в консоли пропишите
```
ngrok http 5000
```
Структура команды '**ngrok http 5000**'
- **ngrok** - утилита для создания туннеля к localhost.
- **http** - протокол, по которому проходят запросы
- **5000** - порт, на котором запущен ваш **ЛОКАЛЬНЫЙ** веб-сервер

После запуска команды у вас появистя данное окно.

![2020-09-11_23-09](https://user-images.githubusercontent.com/46131081/92963675-e817fa00-f483-11ea-9698-a30a730fa542.png)

В поле **Forwarding** находится адрес, по которому ваш локальный сервер
стал доступен в интернете. Содержимое данного поля необходимо будет
передать в файле messenger.py при инициализации объекта **Messenger**.

![2020-09-11_23-16](https://user-images.githubusercontent.com/46131081/92964276-e3077a80-f484-11ea-97a9-e6d704e5f9ec.png)

Запускаем проект и радуемся