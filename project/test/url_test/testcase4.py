import requests, pprint

response = requests.get('http://127.0.0.1:8000/search_from/')
print(response.json())
'''
{'ret': 0}
'''