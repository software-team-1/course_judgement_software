import requests, pprint

response = requests.get('http://127.0.0.1:8000/my_account/', auth=('sq', '88888888'))
print(response.json())

'''
{'ret': 0,
 'course_name': '模拟电子技术',
 'course_teacher': '',
 'judges.email': '123123@qq.com',
 'judges.username': 'sq'}
'''