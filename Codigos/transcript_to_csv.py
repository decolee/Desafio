import re
import pandas as pd
'''
# Defina o caminho do arquivo TXT de entrada e o caminho do arquivo CSV de saída
input_file = r'C:\Users\andre\Documents\Kaggle\faltantes2.txt'
output_file = r'C:\Users\andre\Documents\Kaggle\currency2.csv'

# Abra e leia o conteúdo do arquivo TXT
with open(input_file, 'r') as file:
    content = file.read()

# Use expressões regulares para extrair os dados do arquivo
date_pattern = r'\s*"(\d{4}-\d{2}-\d{2})":\s*'
rate_pattern = r'"(USD\w+)":\s*([\d.]+)'

dates = re.findall(date_pattern, content)
rates = re.findall(rate_pattern, content)

# Converta os dados extraídos em um DataFrame do pandas
data = []
i = 0
for date in dates:
    row = {'data': date}
    for _ in range(3):  # Há 3 taxas de câmbio para cada data
        currency, rate = rates[i]
        row[currency] = float(rate)
        i += 1
    data.append(row)

df = pd.DataFrame(data)

# Salve o DataFrame como um arquivo CSV
df.to_csv(output_file, index=False)
'''
import re
import pandas as pd

# Defina o caminho do arquivo TXT de entrada e o caminho do arquivo CSV de saída
input_file = r'C:\Users\andre\Documents\Kaggle\pismodata.txt'
output_file = r'C:\Users\andre\Documents\Kaggle\currencyusd.csv'

# Abra e leia o conteúdo do arquivo TXT
with open(input_file, 'r') as file:
    content = file.read()

# Use expressões regulares para extrair os dados do arquivo
date_pattern = r'\s*"(\d{4}-\d{2}-\d{2})":\s*'
rate_pattern = r'"(USD\w+)":\s*([\d.]+)'

dates = re.findall(date_pattern, content)
rates = re.findall(rate_pattern, content)

# Converta os dados extraídos em um DataFrame do pandas
data = []
i = 0
for date in dates:
    row = {'data': date}
    for _ in range(3):  # Há 3 taxas de câmbio para cada data
        currency, rate = rates[i]
        row[currency] = float(rate)
        i += 1
    data.append(row)

df = pd.DataFrame(data)

# Salve o DataFrame como um arquivo CSV
df.to_csv(output_file, index=False)