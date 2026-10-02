def extrair_titulo_sql(consulta):
    
    linhas = consulta.strip().splitlines()

    for linha in linhas:

        linha = linha.strip()

        if linha.startswith("--"):
            return linha[2:].strip()

    return "Consulta SQL"


def remover_comentarios_sql(consulta):

    linhas = []

    for linha in consulta.splitlines():

        if not linha.strip().startswith("--"):
            linhas.append(linha)

    return "\n".join(linhas).strip()


def print_title(titulo):
    print(" ")
    print(f"{titulo}")
    print(" ")