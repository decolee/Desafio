import requests
from pymongo import MongoClient

# Fazendo a requisição
url = "https://api.apilayer.com/currency_data/timeframe?start_date=2023-03-16&end_date=2020-03-16"
payload = {}
headers = {
  "apikey": "YeAMzndvd2wsvSujKL21yc3UWplNtdV4"
}
response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text

# Salvando o resultado em um arquivo de texto
with open("resultado.txt", "w") as arquivo:
    arquivo.write(result)

# Lendo o conteúdo do arquivo de texto
with open("resultado.txt", "r") as arquivo:
    conteudo = arquivo.read()

# Conectando ao MongoDB
client = MongoClient("mongodb://usuario:andre@localhost:27017")
db = client['pismo']
collection = db['pismodata']

# Inserindo o conteúdo no MongoDB
documento = {
    "data": conteudo
}
collection.insert_one(documento)
