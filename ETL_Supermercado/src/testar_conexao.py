from sqlalchemy import text
from config import engine_cdb

print("Iniciando teste de conexão...")

try:
    with engine_cdb.connect() as conn:
        resultado = conn.execute(text("SELECT 1"))

        print("Conexão realizada com sucesso!")
        print("Resultado:", resultado.scalar())

except Exception as erro:
    print("Erro ao conectar ao PostgreSQL:")
    print(erro)