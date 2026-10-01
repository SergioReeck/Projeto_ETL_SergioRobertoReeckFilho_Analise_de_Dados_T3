from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

url = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="postgres",
    host="localhost",
    port=5432,
    database="postgres",
)

engine = create_engine(url, isolation_level="AUTOCOMMIT")

with engine.connect() as conn:
    conn.execute(
        text("CREATE DATABASE etl_vendas_supermercado;")
    )

print("Banco criado com sucesso!")