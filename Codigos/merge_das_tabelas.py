import pandas as pd

# Defina os caminhos dos arquivos de entrada e saída
coffee_csv = r'C:\Users\andre\Documents\Kaggle\PISMO\Desafio\coffee.csv'
currency_csv = r'C:\Users\andre\Documents\Kaggle\PISMO\Desafio\currency.csv'
output_csv = r'C:\Users\andre\Documents\Kaggle\PISMO\Desafio\coffee_gold.csv'

# Leia os arquivos CSV como DataFrames do pandas
coffee_df = pd.read_csv(coffee_csv)
currency_df = pd.read_csv(currency_csv)

# Faça a junção dos DataFrames com base nas colunas de data
merged_df = coffee_df.merge(currency_df, left_on='Date', right_on='data', how='left')

# Crie novas colunas para o volume multiplicado pelas taxas de câmbio
merged_df['Volume_USDBRL'] = merged_df['Volume'] * merged_df['USDBRL']
merged_df['Volume_USDCLP'] = merged_df['Volume'] * merged_df['USDCLP']
merged_df['Volume_USDEUR'] = merged_df['Volume'] * merged_df['USDEUR']

# Remova a coluna 'data' duplicada
merged_df.drop('data', axis=1, inplace=True)

# Salve o DataFrame resultante em um novo arquivo CSV
merged_df.to_csv(output_csv, index=False)
