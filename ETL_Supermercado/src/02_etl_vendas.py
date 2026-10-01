import pandas as pd
from pathlib import Path
from normalizacao import imprimir_titulo

imprimir_titulo("Início do processo de ETL...")

# Extração do arquivo raw_vendas_exportada.csv para o DataFrame
print("\nExtraindo dados do arquivo raw_vendas_exportada.csv...")
df = pd.read_csv(
    "data/raw/raw_vendas_exportada.csv"
)

print("Dados extraídos com sucesso!")
print(f"{len(df)} registros extraídos.")
imprimir_titulo("Colunas:")
print(df.columns.tolist())


# Renomeação das colunas
imprimir_titulo("Renomeando colunas...")
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

imprimir_titulo("Colunas após renomeação:")
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

imprimir_titulo("Tipos de dados após conversão:")
print(df.dtypes)


# Verificação de datas inválidas
imprimir_titulo("Verificação de datas inválidas:")
datas_convertidas = pd.to_datetime(
    df['data_venda'],
    format='%m/%d/%Y',
    errors='coerce'
)

print(datas_convertidas.isna().sum())


# Verificação de valores nulos
imprimir_titulo(f"Valores nulos por coluna:")
print(df.isnull().sum())


# Verificação de duplicidades
imprimir_titulo("Quantidade de registros duplicados:")
print(df.duplicated().sum())

# Exportação do DataFrame para CSV tratado
imprimir_titulo("Exportando DataFrame para CSV...")
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