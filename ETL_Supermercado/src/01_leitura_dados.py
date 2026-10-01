import pandas as pd
from config import engine_etl_vendas_supermercado
from normalizacao import imprimir_titulo


# Leitura da tabela Raw para o DataFrame
df = pd.read_sql(
    "SELECT * FROM vendas.raw_vendas",
    engine_etl_vendas_supermercado
)


# Informações gerais do DataFrame
imprimir_titulo("Informações das colunas:")
print(df.info())


# Exibição das primeiras linhas do DataFrame
imprimir_titulo("Primeiras linhas:")
print(df.head(10))


# Exibição das últimas linhas do DataFrame
imprimir_titulo("Últimas linhas:")
print(df.tail(10))


# Verificação de valores nulos
imprimir_titulo("Valores nulos:")    
print(df.isnull().sum())


# Verificação de estatísticas
imprimir_titulo("Estatísticas:")
print(df.describe(include="all"))


# Tipos de data e hora
imprimir_titulo("Data e Hora:")
print(df[["Date", "Time"]].head(10))


# Quantidade de registros do DataFrame
imprimir_titulo("Quantidade de registros:")
print(len(df))

# Exportação para CSV
imprimir_titulo("Exportando para CSV...")
df.to_csv(
    "data/raw/raw_vendas_exportada.csv",
    index=False,
    encoding="utf-8"
)

print("Dados exportados com sucesso!")
print(f"{len(df)} registros exportados para raw_vendas_exportada.csv")