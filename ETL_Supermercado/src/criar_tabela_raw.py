from sqlalchemy import text
from config import engine_etl_vendas_supermercado

sql_criar_schema = """
CREATE SCHEMA IF NOT EXISTS vendas;
"""

sql_criar_tabela_raw = """
CREATE TABLE vendas.raw_vendas (
    "Invoice ID" VARCHAR(50),
    "Branch" VARCHAR(10),
    "City" VARCHAR(100),
    "Customer type" VARCHAR(50),
    "Gender" VARCHAR(20),
    "Product line" VARCHAR(150),
    "Unit price" NUMERIC(10,2),
    "Quantity" INTEGER,
    "Tax 5%" NUMERIC(10,2),
    "Sales" NUMERIC(12,2),
    "Date" VARCHAR(50),
    "Time" VARCHAR(50),
    "Payment" VARCHAR(50),
    "cogs" NUMERIC(12,2),
    "gross margin percentage" NUMERIC(10,2),
    "gross income" NUMERIC(12,2),
    "Rating" NUMERIC(4,2)
);
"""

try:
    with engine_etl_vendas_supermercado.begin() as conn:

        conn.execute(text(sql_criar_schema))
        conn.execute(text(sql_criar_tabela_raw))

    print("Schema 'vendas' criado/verificado com sucesso!")
    print("Tabela 'vendas.raw_vendas' criada/verificada com sucesso!")

except Exception as erro:
    print("Erro ao criar schema ou tabela:")
    print(erro)