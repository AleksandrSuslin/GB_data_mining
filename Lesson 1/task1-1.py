import requests
import json


user = 'AleksandrSuslin'
url = f"https://api.github.com/users/{user}/repos"
params = {'type': 'all'}
response = requests.get(url, params=params)

j_data = response.json()


repositories = []

for n in range(len(j_data)):
    repositories.append(j_data[n]['name'])


print(f"Репозитории пользователя {user}: {repositories}")

with open ('repositories.json', 'w') as repos:
    json.dump(j_data, repos)