
# https://requests.readthedocs.io/
import requests

banner = '''
╔═╗╔╦╗╔═╗╦═╗╦ ╦╔═╗╦═╗╔═╗  ╦  ╔═╗╔═╗╦╔═╦ ╦╔═╗
╚═╗ ║ ╠═╣╠╦╝║║║╠═╣╠╦╝╚═╗  ║  ║ ║║ ║╠╩╗║ ║╠═╝
╚═╝ ╩ ╩ ╩╩╚═╚╩╝╩ ╩╩╚═╚═╝  ╩═╝╚═╝╚═╝╩ ╩╚═╝╩  
'''
print(banner)
print("Welkom in mijn script, van welk nummer wil je de Starwars character zien?")

url = "https://swapi.dev/api/people/"
nummer = input("Geef nummer: ")

res = requests.get(url + nummer)

if res.status_code != 200:
  print("Helaas niemand gevonden")
else:
  print("We hebben iemand gevonden")
  naam = res.json()["name"]
  by = res.json()["birth_year"]
  print(naam)
  print(by)

print("Bedankt voor het gebruiken van onze tool!")
