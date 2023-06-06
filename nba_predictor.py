import requests
import json

url = 'http://localhost:8082/predict'

data = {
    'GP': 80,
    'MIN': 30,
    'PTS': 10,
    'FGM': 5,
    'FGA': 15,
    'FG%': 0.333,
    '3P Made': 1,
    '3PA': 3,
    '3P%': 0.333,
    'FTM': 2,
    'FTA': 2,
    'FT%': 1.0,
    'OREB': 1,
    'DREB': 3,
    'REB': 4,
    'AST': 3,
    'STL': 1,
    'BLK': 0,
    'TOV': 2,
    'TARGET_5Yrs': 1
}

headers = {
    'Content-type': 'application/json'
}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.json())

