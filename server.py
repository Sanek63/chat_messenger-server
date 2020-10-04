import time
from datetime import datetime

from flask import Flask, request

from database.login import Login_Database

app = Flask(__name__)
db = []


@app.route('/')
def hello():
    return "Добро пожаловать в мессенджер <a href='/status'>Статус</a>"


@app.route('/status')
def status():
    dn = datetime.now()
    return {
        "status": True,
        "name": "Messenger",
        "time": dn.strftime("%d.%m.%Y %H:%M:%S"),
        "messages_count": len(db),
        "user_count": len(set([message['name'] for message in db]))
    }


@app.route('/send', methods=['POST'])
def send():
    data = request.json

    db.append({
        'id': len(db),
        'name': data['name'],
        'text': data['text'],
        'timestamp': time.time()
    })
    return {"ok": True}


@app.route('/messages')
def messages():
    if 'after_timestamp' in request.args:
        after_timestamp = float(request.args['after_timestamp'])
    else:
        after_timestamp = 0

    max_limit = 5

    after_id = 0
    for message in db:
        if message['timestamp'] > after_timestamp:
            break
        after_id += 1
    return {'messages': db[after_id: after_id + max_limit]}


@app.route('/registration', methods=['POST'])
def registration_user():
    args = request.json

    username = args['username']
    password = args['password']

    query = "SELECT * FROM users WHERE username = '{}'".format(args['username'])
    cursor.execute(query)
    result = bool(cursor.rowcount)

    if result:
        return {'is_exist': True}
    else:
        query = "INSERT INTO users VALUES ('{}','{}')".format(username, password)
        cursor.execute(query)
        conn.commit()
        return {'is_exist': False}


@app.route('/login', methods=['POST'])
def login():
    data = request.json

    username = data['username']
    password = data['password']

    query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(
        username, password
    )

    cursor.execute(query)
    result = bool(cursor.rowcount)

    return {'is_logged': result}


if __name__ == '__main__':
    login_database = Login_Database('users_messenger')
    cursor = login_database.conn.cursor()
    conn = login_database.conn

    app.run()
