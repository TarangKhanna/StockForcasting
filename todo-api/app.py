#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for, flash
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS, cross_origin
import sys
import mysql.connector
#initilization
app = Flask(__name__)
CORS(app)
id = 0
# extenstions
auth = HTTPBasicAuth()

cnx = mysql.connector.connect(user='root', password='hellostocks', host='localhost', database='stocks')

# Other Vars
Predicted_Prices = {}
Predicted_Prices['Google'] = '55.00'
Predicted_Prices['Apple'] = '53.00'
tasks = [
    {
        'userId': 2,
        'firstName': u'Tarang',
        'lastName': u'Khanna',
        'age': u'20',
        'phoneNumber': u'4794228206',
        'password': u'Khanna',
        'email': u'TarangKhanna',
    }
]

@auth.get_password
def get_password(username):
    # compare passwords and usernames
    if username == 'miguel':
        return 'python'
    if username == 'a':
        return 'b'
    return None

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

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks', methods=['GETUSERDATA'])
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


@app.route('/todo/api/v1.0/tasks', methods=['ADDUSER'])
def add_user():
    if not request.json:
        print("aborted here")
        abort(400)

    global id
    id += 1
    
    new_user = (id, request.json['firstName'], request.json['lastName'], request.json['age'], request.json['phoneNumber'], request.json['password'], request.json['email'])
    cursor = cnx.cursor()
    add_user = ("INSERT INTO USER_BASIC_INFO "
                   "(userID, firstName, lastName, age, phoneNumber, password, email) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)")

    cursor.execute(add_user, new_user)

    cnx.commit()
    cursor.close()
    return jsonify({'new_user': new_user}), 201


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

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['ADDSTOCKS'])
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

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

##################
# Authentication #
##################
@app.route('/ss/v1.0/login', methods=['POST'])
def login():
    #print("here")
    if not request.json:
        abort(400)  # no request.json
    data = request.get_json()
    email = data.get('email')
    password = data.get('pswd')

    if username is None or password is None:
        abort(400)    # missing arguments

    if get_password(username) == password:
        ret = jsonify({"response" : [{"dispName" : email}]})
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
