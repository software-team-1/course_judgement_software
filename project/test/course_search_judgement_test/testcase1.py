import requests, pprint

#搜索功能测试

payload = {'q': '模拟', 'user': 'sq'}

response = requests.post('http://127.0.0.1:8000/search_from/', payload)
print(response.json())