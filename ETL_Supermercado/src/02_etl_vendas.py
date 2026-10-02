import pandas as pd
from pathlib import Path
from normalizacao import print_title

print_title("Início do processo de ETL...")

# Extração do arquivo raw_vendas.csv para o DataFrame
print("Extraindo dados do arquivo raw_vendas.csv...")

df = pd.read_csv(
    "data/raw/raw_vendas.csv"
)

print("Dados extraídos com sucesso!")
print(f"{len(df)} registros extraídos.")
print_title("Colunas:")
print(df.columns.tolist())

# Renomeação das colunas
print_title("Renomeando colunas...")

df = df.rename(columns={
    "Invoice ID": "id_venda",
    "Branch": "filial",
    "City": "cidade",
    "Customer type": "tipo_cliente",
    "Gender": "genero",
    "Product line": "linha_produto",
    "Unit price": "preco_unitario",
    "Quantity": "quantidade",
    "Tax 5%": "imposto",
    "Sales": "valor_total",
    "Date": "data_venda",
    "Time": "hora_venda",
    "Payment": "forma_pagamento",
    "cogs": "custo_mercadoria",
    "gross margin percentage": "margem_percentual",
    "gross income": "receita_bruta",
    "Rating": "avaliacao"
})

print_title("Colunas após renomeação:")
print(df.columns.tolist())

# Conversão da data
df["data_venda"] = pd.to_datetime(
    df["data_venda"],
    format="%m/%d/%Y"
).dt.date

# Conversão da hora
df["hora_venda"] = pd.to_datetime(
    df["hora_venda"],
    format="%I:%M:%S %p"
).dt.time

# Conversão das colunas numéricas
colunas_numericas = [
    "preco_unitario",
    "quantidade",
    "imposto",
    "valor_total",
    "custo_mercadoria",
    "margem_percentual",
    "receita_bruta",
    "avaliacao"
]

for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(
        df[coluna],
        errors="coerce"
    )

print_title("Tipos de dados após conversão:")
print(df.dtypes)

# Verificação de datas inválidas
print_title("Verificação de datas inválidas:")
datas_convertidas = pd.to_datetime(
    df['data_venda'],
    format='%m/%d/%Y',
    errors='coerce'
)
print(datas_convertidas.isna().sum())

# Verificação de valores nulos
print_title(f"Valores nulos por coluna:")
print(df.isnull().sum())

# Verificação de duplicidades
print_title("Quantidade de registros duplicados:")
print(df.duplicated().sum())

# Exportação do DataFrame para CSV tratado
print_title("Exportando DataFrame para CSV...")
pasta_saida = Path('data/processed')
arquivo_saida = pasta_saida / 'vendas_tratadas.csv'

pasta_saida.mkdir(parents=True, exist_ok=True)

if arquivo_saida.exists():
    print("Arquivo já existe. Será atualizado.")
else:
    print("Arquivo criado com sucesso!")

df.to_csv(
    arquivo_saida,
    index=False,
    encoding='utf-8-sig'
)
print(f"Arquivo salvo em: {arquivo_saida}")