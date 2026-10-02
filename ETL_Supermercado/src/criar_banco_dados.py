import os

from sqlalchemy import text
from config import engine_cdb

print("Iniciando criação do banco de dados...")

# sql_banco_de_dados = """
# CREATE DATABASE {db_name};
# """.format(db_name=os.getenv('DB_NAME'))

sql_banco_de_dados = """
CREATE DATABASE etl_supermercado;
"""

try:
    with engine_cdb.connect() as conn:

        conn.execute(text(sql_banco_de_dados))

    print(f"Banco de dados '{os.getenv('DB_NAME')}' criado com sucesso!")

except Exception as erro:
    print("Erro ao criar banco de dados:")
    print(erro)