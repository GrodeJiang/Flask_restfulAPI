import requests

sample =  {
            'name'  :  'Tim',
            'sex' : 'male',
            'height' : 168,
            'weight' : 67
            }
newHeaders = {'Content-type': 'application/json'}

response  = requests.put('http://127.0.0.1:5000/api/students/3', json=sample,headers=newHeaders)
print(response.json())