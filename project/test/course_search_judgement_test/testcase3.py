import requests, pprint

#删除评论功能测试

payload = {'course_id': 1, 'user': 'sq'}

response = requests.post('http://127.0.0.1:8000/search_from/', payload)
print(response.json())