from flask import Flask, jsonify, abort, request

app = Flask(__name__)

students = [
        {
            'ID' : 1,
            'name'  :  'John',
            'sex' : 'male',
            'height' : '163',
            'weight' : '57'
            },
        {
            'ID' : 2,
            'name'  :  'Amy',
            'sex' : 'female',
            'height' : '160',
            'weight' : '50'
            },
        {
            'ID' : 3,
            'name'  :  'Alex',
            'sex' : 'male',
            'height' : '180',
            'weight' : '97'
            },
        {
            'ID' : 4,
            'name'  :  'Mary',
            'sex' : 'female',
            'height' : '165',
            'weight' : '75'
            }
    ]

@app.route('/')
def homepage():
    return "Welcome"

@app.route('/api/students', methods = ['GET', 'POST'])
def students_control():
    if request.method == 'GET':
        return jsonify({'student':students})
    elif request.method == 'POST':
        if not request.json or not 'name' in request.json:
            abort(400)        
        jsonData = dict(request.json)
        student = {
            'ID': students[-1]['ID'] + 1,
            'name': jsonData.get('name', ''),
            'sex': jsonData.get('sex', ''),
            'height': jsonData.get('height', ''),
            'weight': jsonData.get('weight', '')
        }
        students.append(student)
        return jsonify({'student': student}), 201        

@app.route('/api/students/<int:ID>', methods = ['GET', 'PUT', 'DELETE'])
def student_control(ID):
    if request.method == 'GET':
        student = list(filter(lambda s : s['ID'] == ID, students))
        if len(student) == 0:
            abort(404)
        return jsonify({'student': student[0]}), 201
    elif request.method == 'PUT':
        student = list(filter(lambda s : s['ID'] == ID, students))
        if len(student) == 0:
            abort(404)
        if not request.json :
            abort(400)    
        jsonData = dict(request.json)
        if 'name' in request.json and not isinstance(jsonData['name'], str):
            abort(400)    
        if 'sex' in request.json and not isinstance(jsonData['sex'], str):
            abort(400)    
        if 'height' in request.json and not isinstance(jsonData['height'], int):
            abort(400)    
        if 'weight' in request.json and not isinstance(jsonData['weight'], int):
            abort(400)    
        student[0]['name'] = jsonData.get('name', students[ID]['name'] )
        student[0]['sex'] = jsonData.get('sex', students[ID]['sex'] )
        student[0]['height'] = jsonData.get('height', students[ID]['height'] )
        student[0]['weight'] = jsonData.get('weight', students[ID]['weight'] )
        return jsonify({'student': student[0]}), 201
    elif request.method == 'DELETE':
        student = list(filter(lambda s : s['ID'] == ID, students))
        if len(student) == 0:
            abort(404)
        students.remove(student[0])
        return jsonify({'result': True}), 201

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug = True)