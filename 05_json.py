import json
with open('myinfo.json', encoding='utf-8') as f:
    data= json.load(f)
print(type(data))
print(data)