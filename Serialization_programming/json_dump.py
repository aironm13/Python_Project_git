import json


a = [1, 2, 3, 4, 5]

with open('b.txt', 'w') as f:
    json.dump(a, f)