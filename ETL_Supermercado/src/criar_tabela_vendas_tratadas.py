from sqlalchemy import text
from config import engine_etl

print("Iniciando criação/verificação do(s) schema(s) e tabela(s)...")

sql_criar_schema = """
CREATE SCHEMA IF NOT EXISTS vendas;
"""

sql_criar_tabela_raw = """
CREATE TABLE vendas.vendas_tratadas (
    id_venda VARCHAR(50) PRIMARY KEY NOT NULL,
    filial VARCHAR(10) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    tipo_cliente VARCHAR(50),
    genero VARCHAR(20),
    linha_produto VARCHAR(150) NOT NULL,
    preco_unitario NUMERIC(10,2)
        CHECK (preco_unitario >= 0),
    quantidade INTEGER
        CHECK (quantidade > 0),
    imposto NUMERIC(10,2)
        CHECK (imposto >= 0),
    valor_total NUMERIC(12,2)
        CHECK (valor_total >= 0),
    data_venda DATE,
    hora_venda TIME,
    forma_pagamento VARCHAR(50) NOT NULL,
    custo_mercadoria NUMERIC(12,2)
        CHECK (custo_mercadoria >= 0),
    margem_percentual NUMERIC(10,2),
    receita_bruta NUMERIC(12,2)
        CHECK (receita_bruta >= 0),
    avaliacao NUMERIC(4,2)
        CHECK (avaliacao >= 0 AND avaliacao <= 10)
);
"""

try:
    with engine_etl.begin() as conn:

        conn.execute(text(sql_criar_schema))
        conn.execute(text(sql_criar_tabela_raw))

    print("Schema 'vendas' criado/verificado com sucesso!")
    print("Tabela 'vendas.vendas_tratadas' criada/verificada com sucesso!")

except Exception as erro:
    print("Erro ao criar schema ou tabela:")
    print(erro)