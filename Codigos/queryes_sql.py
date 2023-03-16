import pandas as pd
from sqlalchemy import create_engine

# Conecte-se ao banco de dados SQLite
engine = create_engine("sqlite:///exchange_rates.db")

# Consultas SQL
sql_queries = {
    "maior_volume_negociado": """
        -- Insira sua consulta SQL aqui
    """,
    "total_cafe_negociado_por_ano": """
        -- Insira sua consulta SQL aqui
    """,
    "media_volume_negociado_mensal_anual": """
        -- Insira sua consulta SQL aqui
    """
}

# Execute as consultas e salve os resultados em arquivos CSV
for query_name, query in sql_queries.items():
    result = pd.read_sql_query(query, engine)
    result.to_csv(f"{query_name}.csv", index=False)
