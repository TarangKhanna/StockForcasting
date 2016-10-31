#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for, flash
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS, cross_origin
import sys
import cx_Oracle

#initilization
app = Flask(__name__)
CORS(app)

# extenstions
auth = HTTPBasicAuth()

conn_str = u'user/password@host:port/service'
conn = cx_Oracle.connect(conn_str)
c = conn.cursor()
c.execute(u'select your_col_1, your_col_2 from your_table')
for row in c:
    print row[0], "-", row[1]

# Other Vars
Predicted_Prices = {}
Predicted_Prices['Google'] = '55.00'
Predicted_Prices['Apple'] = '53.00'
tasks = [
    {
        'id': 1,
        'name': u'Atul Aneja',
        'MyStocks': u'Google',
        'Predicted_Price': u'%s'%Predicted_Prices['Google']
    },
    {
        'id': 2,
        'name': u'Tarang Khanna',
        'MyStocks': u'Apple',
        'Predicted_Price': u'%s'%Predicted_Prices['Apple']
    }
]

@auth.get_password
def get_password(username):
    # compare passwords and usernames
    if username == 'miguel':
        return 'python'
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

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'name' in request.json:
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
    print("here")
    if not request.json:
        abort(400)  # no request.json
    data = request.get_json()
    username = data.get('uname')
    password = data.get('pswd')

    if username is None or password is None:
        abort(400)    # missing arguments

    if get_password(username) == password:
        return (jsonify({'response': "Welcome " + username}), 201)
    else:
        return (jsonify({'response': "Incorrect Username or Password. Please try again"}), 201)

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
