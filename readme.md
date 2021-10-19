# API Document

## 欄位說明

| 欄位          | 內容          |
| ------------- |:-------------:|
| ID            | 學生ID<int>   |
| name          | 名字<string>  |
| sex           | 性別<string>  |
| height        | 身高<int>     |
| weight        | 體重<int>     |

## 取得所有學生資料  
`/api/students`     
* Method : GET  
* Success Response:  
  * Code: 201  
  content:  
  ```
  [{
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
    }]
  ```
  
## 取得單一學生資料  
`/api/students/ID`   
* Method : GET  
* Required: ID<int>  
* Success Response:  
  * Code: 201  
  content:  
  ```
  {
    'ID' : 1,
    'name'  :  'John',
    'sex' : 'male',
    'height' : '163',
    'weight' : '57'
  }
  ```
 
* Error Response:  
  * Code: 404  
  ID not exist

## 新增學生
`/api/students/`   
* Method : `POST`  
* Data Params:
```
{
    'name'  :  'Tim',
    'sex' : 'male',
    'height' : 168,
    'weight' : 67
}
```
* Success Response:  
  * Code: 201  
  content:  
  ```
  {
    'ID' : 10,
    'name'  :  'Tim',
    'sex' : 'male',
    'height' : 168,
    'weight' : 67
  }
  ```
 
* Error Response:  
  * Code: 400

## 更新學生資料
`/api/students/ID`   
* Method : PUT  
* Required: ID<int>   
* Data Params:
```
{
    'name'  :  'John',
    'sex' : 'male',
    'height' : '168',
    'weight' : '56'
}
```
* Success Response:  
  * Code: 201  
  content:  
  ```
  {
    'ID' : 1,
    'name'  :  'John',
    'sex' : 'male',
    'height' : '161',
    'weight' : '56'
  }
  ```
 
* Error Response:  
  * Code: 400  
  
  OR
  * Code: 404  
  ID not exist  

## 刪除學生資料  
`/api/students/ID`   
* Method : DELETE  
* Required: ID<int>  
* Success Response:  
  * Code: 201  
  content:  
  ```
  {'result': True}
  ```
* Error Response:  
  * Code: 404  
  ID not exist