import pandas as pd
from config import engine_etl
from normalizacao import print_title

# Leitura da tabela Raw para o DataFrame
df = pd.read_sql(
    "SELECT * FROM vendas.raw_vendas",
    engine_etl
)

# Informações gerais do DataFrame
print_title("Informações das colunas:")
print(df.info())

# Exibição das primeiras linhas do DataFrame
print_title("Primeiras linhas:")
print(df.head(10))

# Exibição das últimas linhas do DataFrame
print_title("Últimas linhas:")
print(df.tail(10))

# Verificação de valores nulos
print_title("Valores nulos:")    
print(df.isnull().sum())

# Verificação de estatísticas
print_title("Estatísticas:")
print(df.describe(include="all"))

# Tipos de data e hora
print_title("Data e Hora:")
print(df[["Date", "Time"]].head(10))

# Quantidade de registros do DataFrame
print_title("Quantidade de registros:")
print(len(df))

# Exportação para CSV
print_title("Exportando para CSV...")
df.to_csv(
    "data/raw/raw_vendas.csv",
    index=False,
    encoding="utf-8"
)

print("Dados exportados com sucesso!")
print(f"{len(df)} registros exportados para raw_vendas.csv")