import requests, pprint

response = requests.get('http://127.0.0.1:8000/search_result/thumb/')
print(response.json())
'''
{'ret': 0}
'''