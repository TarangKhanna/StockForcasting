#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': u'Atul Aneja',
        'MyStocks': u'Google', 
        'Predicted_Price': u'price'
    },
    {
        'id': 2,
        'name': u'Tarang Khanna',
        'MyStocks': u'Apple',
        'Predicted_Price': u'price' 
    }
]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
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

if __name__ == '__main__':
    app.run(debug=True)