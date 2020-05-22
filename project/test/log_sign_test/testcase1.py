import requests, pprint

#登录功能测试

payload = {'user': 'sq', 'password': '88888888'}

response = requests.get('http://127.0.0.1:8000/login/', payload)
print(response.json())