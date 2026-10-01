import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

# Conexão etl_vendas_supermercado

engine_etl_vendas_supermercado= create_engine(
    f"postgresql+psycopg2://"
    f"{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}"
    f"/{os.getenv('DB_DATABASE')}"
)