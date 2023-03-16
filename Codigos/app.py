import requests
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Table, MetaData
from datetime import datetime, timedelta

# Configurações
API_KEY = "YeAMzndvd2wsvSujKL21yc3UWplNtdV4"
BASE_URL = "http://api.currencystack.io/historical"

# Moedas a serem consultadas
currencies = ["BRL", "EUR", "CLP"]

# Função para obter taxas de câmbio
def get_exchange_rates(date, currencies, api_key):
    params = {
        "access_key": api_key,
        "date": date,
        "currencies": ",".join(currencies),
        "format": 1
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

# Obtenha taxas de câmbio dos últimos 30 dias
start_date = datetime.now() - timedelta(days=30)
date_range = [start_date + timedelta(days=i) for i in range(31)]

exchange_rates = []

for date in date_range:
    date_str = date.strftime("%Y-%m-%d")
    result = get_exchange_rates(date_str, currencies, API_KEY)
    if "quotes" in result:
        for currency, rate in result["quotes"].items():
            exchange_rates.append({"Date": date_str, "Currency": currency[3:], "Rate": rate})

# Criar tabela exchange_rates
metadata = MetaData()

exchange_rates_table = Table(
    "exchange_rates",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("Date", Date),
    Column("Currency", String(3)),
    Column("Rate", Float)
)

# Criar a tabela no banco de dados SQLite
engine = create_engine("sqlite:///exchange_rates.db")
metadata.create_all(engine)

# Converter os dados em um DataFrame do Pandas
df = pd.DataFrame(exchange_rates)

# Salvar os dados na tabela exchange_rates do banco de dados SQLite
df.to_sql("exchange_rates", engine, if_exists="append", index=False)
