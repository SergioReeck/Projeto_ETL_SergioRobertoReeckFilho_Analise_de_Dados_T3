import pandas as pd
import kagglehub

from pathlib import Path
from config import engine_etl


# CSV_PATH = "data/raw/SuperMarket Analysis.csv"

# file_path = Path(kagglehub.dataset_download("faresashraf1001/supermarket-sales"))
# print("Path to dataset files:", file_path)

file_path = Path(
    kagglehub.dataset_download("faresashraf1001/supermarket-sales")
)

print("Path to dataset files:", file_path)

def load_raw():

    print("Extraindo dados do arquivo CSV...")
    
    # 1. Ler o CSV
    df = pd.read_csv(file_path / "SuperMarket Analysis.csv")
    print(df.columns.tolist())
    print(f"Arquivo lido: {len(df)} registros")

    # 2. Carregar na tabela Raw
    df.to_sql(
        "raw_vendas",
        engine_etl,
        schema="vendas",
        if_exists="append",
        index=False
    )
    
    print("Carga Raw concluída!")


if __name__ == "__main__":
    load_raw()