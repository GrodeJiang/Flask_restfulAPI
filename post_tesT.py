import requests

sample =  {
            'name'  :  'Tim',
            'sex' : 'male',
            'height' : 168,
            'weight' : 67
            }
newHeaders = {'Content-type': 'application/json'}

response  = requests.post('http://127.0.0.1:5000/api/students/create', json=sample,headers=newHeaders)
print(response.json())