import requests, pprint

response = requests.get('http://127.0.0.1:8000/my_account/', auth=('sq', '88888888'))
print(response.json())
'''
{'ret': 0}
'''
