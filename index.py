import json
import re

# selecionar o json
with open('tasks.json') as file:
    tasks = json.load(file)

nao_feitas = tasks['tasks'][0]['nao-feitas']
feitas = tasks['tasks'][0]['feitas']

print(f'Não feitas: {nao_feitas}\n')
print(f'Feitas: {feitas}')

while True:
    comando = input("> ")

    # adicionar item
    if re.findall('^add', comando) == ['add']:
        comando = re.sub('^add ', '', comando)
        nao_feitas.append(comando)
    # remover item especifico
    elif re.findall('^rm', comando) == ['rm']:
        comando = re.sub('^rm ', '', comando)
        nao_feitas.pop(int(comando))
    # comando para remover todos não feitos
    elif re.findall('^rall', comando) == ['rall']:
        nao_feitas.clear()
    elif re.findall('^mark', comando) == ['mark']:
        comando = re.sub('^mark ', '', comando)
        feitas.append(nao_feitas[int(comando)])
        nao_feitas.pop(int(comando))

    print(f'Não feitas: {nao_feitas}\n')
    print(f'Feitas: {feitas}')

    # escrever no json
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
