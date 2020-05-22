import requests, pprint

#注册功能测试

payload = {'username': 'sq',
           'password1': '88888888',
           'password2': '88888888',
           'email': '123123@qq.com',
           'student_number': '123123123',
           'phone': '1102108579'}

response = requests.get('http://127.0.0.1:8000/login/', payload)
print(response.json())