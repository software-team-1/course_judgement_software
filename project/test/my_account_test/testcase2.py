import requests, pprint

payload = {'course_id': 1}

response = requests.get('http://127.0.0.1:8000/modify_judgement/', auth=('sq', '88888888'))
print(response.json())
