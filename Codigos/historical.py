import requests

url = "https://api.apilayer.com/currency_data/timeframe?start_date=2023-02-15&end_date=2023-02-15"

payload = {}
headers= {
  "apikey": "YeAMzndvd2wsvSujKL21yc3UWplNtdV4"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text