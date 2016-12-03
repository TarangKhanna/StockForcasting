#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for, flash
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS, cross_origin
import sys
import mysql.connector
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#initilization
app = Flask(__name__)

CORS(app, supports_credentials=True)
id = 0
# extenstions
auth = HTTPBasicAuth()


CORS(app)
# extenstions
auth = HTTPBasicAuth()

cnx = mysql.connector.connect(user='root', password='hellostocks', host='localhost', database='stocks')

# Other Vars
# Predicted_Prices = {}
# Predicted_Prices['Google'] = '55.00'
# Predicted_Prices['Apple'] = '53.00'
# tasks = [
#     {
#         'userId': 2,
#         'firstName': u'Tarang',
#         'lastName': u'Khanna',
#         'age': u'20',
#         'phoneNumber': u'4794228206',
#         'password': u'Khanna',
#         'email': u'TarangKhanna',
#     }
# ]

@auth.get_password
def get_password(username):
    # compare passwords and usernames
    if username == 'miguel':
        return 'python'
    if username == 'a':
        return 'b'

    cursor = cnx.cursor()
    cursor.execute("SELECT password FROM USER_BASIC_INFO WHERE email = \"%s\"", username);

    data = cursor.fetchone()
    cnx.commit()
    cursor.close()

    return data[0]

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})

# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         abort(404)
#     return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/getUserData', methods=['GET'])
def get_user_data():
    if not request.json:
        print("aborted here")
        abort(400)

    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM USER_BASIC_INFO WHERE firstName = %s AND lastName = %s", [request.json['firstName'], request.json['lastName']])

    data = cursor.fetchone()
    cnx.commit()
    cursor.close()

    return jsonify({"data": data}), 201


@app.route('/todo/api/v1.0/tasks/addStocks', methods=['POST'])
def add_stock():
    if not request.json:
        print("aborted here")
        abort(400)

    cursor = cnx.cursor()
    cursor.execute("SELECT COUNT(*) FROM USER_BASIC_INFO;")
    data = cursor.fetchone()

    new_stock = (data[0] + 1, request.json['stockID'], request.json['trend'], request.json['userID'])

    add_stock = ("INSERT INTO STOCK_WATCH_LIST "
                   "(stockID, trend, userID, age, phoneNumber, password, email) "
                   "VALUES (%s, %s, %s)")



    cursor.execute(add_stock, new_stock)

    cnx.commit()
    cursor.close()
    return (jsonify({'data':data}), 201)

@app.route('/todo/api/v1.0/tasks/addUser', methods=['POST'])
def add_user():
    if not request.json:
        print("aborted here")
        abort(400)


    global id
    id += 1

    # new_user = (id, request.json['firstName'], request.json['lastName'], request.json['age'], request.json['phoneNumber'], request.json['password'], request.json['email'])

    cursor = cnx.cursor()
    cursor.execute("SELECT COUNT(*) FROM USER_BASIC_INFO;")
    data = cursor.fetchone()

    new_user = (data[0] + 1, request.json['firstName'], request.json['lastName'], request.json['age'], request.json['phoneNumber'], request.json['password'], request.json['email'])


    add_user = ("INSERT INTO USER_BASIC_INFO "
                   "(userID, firstName, lastName, age, phoneNumber, password, email) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)")

    cursor.execute(add_user, new_user)

    cnx.commit()
    cursor.close()
    return (jsonify({'new_user': new_user}), 201)


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'name' in request.json:
        print("aborts here")
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'MyStocks': request.json.get('MyStocks', ""),
        'Predicted_Price': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>/addStocks', methods=['POST'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'MyStocks' in request.json and type(request.json['MyStocks']) is not unicode:
        abort(400)
    if 'Predicted_Price' in request.json and type(request.json['Predicted_Price']) is not unicode:
        abort(400)
    task[0]['name'] = request.json.get('name', task[0]['name'])
    task[0]['MyStocks'] = task[0]['MyStocks'] + ", " + request.json.get('MyStocks', task[0]['MyStocks'])
    task[0]['Predicted_Price'] = request.json.get('Predicted_Price', task[0]['Predicted_Price'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


#################
#     Email     #
#################
@app.route('/ss/v1.0/contact', methods=['POST'])
def contact():

    fromaddr = "stockstockr@gmail.com"
    toaddr = "stockstockr@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "SUBJECT OF THE MAIL"

    body = "YOUR MESSAGE HERE"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "StocksOnStocks")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

##################
#    Testing     #
##################
@app.route('/todo/api/o/test')
def test():
    return "testing"


##################
# Authentication #
##################
@app.route('/ss/v1.0/login', methods=['POST'])
def login():
    #print("here")
    if not request.json:
        abort(400)  # no request.json
    data = request.get_json()
    username = data.get('uname')
    password = data.get('pswd')

    if username is None or password is None:
        abort(400)    # missing arguments

    if get_password(username) == password:
        ret = jsonify({"response" : [{"dispName" : username}]})
        return (ret, 201)
    else:
        return (jsonify({"response": "Incorrect Username or Password. Please try again"}), 400)

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

if __name__ == '__main__':
    app.run(debug=True)
