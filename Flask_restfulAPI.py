import json
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

students = [
        {
            'studentID' : 1,
            'name'  :  'John',
            'sex' : 'male',
            'height' : '163',
            'weight' : '57'
            },
        {
            'studentID' : 2,
            'name'  :  'Amy',
            'sex' : 'female',
            'height' : '160',
            'weight' : '50'
            },
        {
            'studentID' : 3,
            'name'  :  'Alex',
            'sex' : 'male',
            'height' : '180',
            'weight' : '97'
            },
        {
            'studentID' : 4,
            'name'  :  'Mary',
            'sex' : 'female',
            'height' : '165',
            'weight' : '75'
            }
    ]

@app.route('/')
def homepage():
    return "Welcome"

@app.route('/api/students', methods = ['GET'])
def get_students():
    return jsonify({'students': students})

@app.route('/api/students/<int:studentID>', methods = ['GET'])
def get_student(studentID):
    student = list(filter(lambda s : s['studentID'] == studentID, students))
    if len(student) == 0:
        abort(404)
    return jsonify({'student': student[0]})

@app.route('/api/students/create', methods = ['POST'])
def create_student():
    if not request.json or not 'name' in request.json:
        abort(400)        
    jsonData = dict(request.json)
    student = {
        'studentID': students[-1]['studentID'] + 1,
        'name': jsonData.get('name', ''),
        'sex': jsonData.get('sex', ''),
        'height': jsonData.get('height', ''),
        'weight': jsonData.get('weight', '')
    }
    students.append(student)
    return jsonify({'student': student}), 201

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug = True)