import requests, pprint

response = requests.get('http://127.0.0.1:8000/add_judgement/')
print(response.json())
'''
{'ret': 0}
'''