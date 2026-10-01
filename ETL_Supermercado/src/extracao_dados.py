import pandas as pd
from config import engine_etl_vendas_supermercado


CSV_PATH = "data/raw/SuperMarket Analysis.csv"



def load_raw():
    print("Extraindo dados do arquivo CSV...")
    # 1. Ler o CSV
    df = pd.read_csv(CSV_PATH)
    print(df.columns.tolist())

    print(f"Arquivo lido: {len(df)} registros")

    # 2. Carregar na tabela Raw
    df.to_sql(
        "raw_vendas",
        engine_etl_vendas_supermercado,
        schema="vendas",
        if_exists="replace",
        index=False
    )

    print("Carga Raw concluída!")


#if __name__ == "__main__":
#    load_raw()