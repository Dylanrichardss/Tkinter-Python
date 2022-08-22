import requests
import json

digmons = requests.get("https://digimon-api.herokuapp.com/api/digimon")
#print(digmons)
print(digmons.text)

dic = json.loads(digmons.text)
#pegar tudo que esta dentro dos digmons e converte para dicionário]

#print(dic[1])
print()

#for item in dic:
#    print(item["name"])

    