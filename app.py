from flask import Flask, jsonify, abort, make_response


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.errorhandler(404)
def not_found(error):
    response = jsonify({'error': 'Not found'})
    return make_response(response, 404)


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):  
    response = []
    for task in tasks:
        if task['id'] == task_id:
            response.append(task)

    if len(response) == 0:
        abort(404)
    return jsonify({'task': response[0]})