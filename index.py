import json

with open('tasks.json') as file:
    tasks = json.load(file) 
    tasks['tasks'][0]['nao-feitas'] = "n"

print(tasks["tasks"][0]["nao-feitas"])

with open('tasks.json', 'w') as file:
    json.dump(tasks, file)

