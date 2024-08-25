import json
data={    
    "name": "항가",
    "birth": "0525",
    "age": 17
}
# with open('myinfo2.json', 'w') as f:
#     json.dump(data, f)
json_data= json.dumps(data,indent=1, ensure_ascii=False)
print(json_data)
print(json.loads(json_data))