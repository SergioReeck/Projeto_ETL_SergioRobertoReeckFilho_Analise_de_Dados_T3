from sqlalchemy import text
from config import engine_etl_vendas_supermercado

print("Iniciando teste de conexão...")

try:
    with engine_etl_vendas_supermercado.connect() as connection:
        resultado = connection.execute(text("SELECT 1"))

        print("Conexão realizada com sucesso!")
        print("Resultado:", resultado.scalar())

except Exception as erro:
    print("Erro ao conectar ao PostgreSQL:")
    print(erro)