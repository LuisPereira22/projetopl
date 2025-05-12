import sys
import csv
from cql_lexer import lexer
from cql_parser import parser
from executor import CommandExecutor

def verificar_colunas():
    with open('observacoes.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        colunas = reader.fieldnames
        print("Colunas do arquivo observacoes.CSV:", colunas)

        # Lê os dados e converte as colunas necessárias para float
        dados_observacoes = {'columns': reader.fieldnames, 'data': [row for row in reader]}
        for row in dados_observacoes['data']:
            row['IntensidadeVentoKM'] = float(row['IntensidadeVentoKM'])  # IntensidadeVentoKM
            row['Temperatura'] = float(row['Temperatura'])  # Temperatura
            row['Radiação'] = float(row['Radiação'])  # Radiação
            row['IntensidadeVento'] = float(row['IntensidadeVento'])  # IntensidadeVento
            row['Humidade'] = float(row['Humidade'])  # Humidade

    with open('estacoes.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        colunas = reader.fieldnames
        print("Colunas do arquivo estacoes.CSV:", colunas)


def processar_entrada_fca(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        # Lê o arquivo e executa linha por linha
        linhas = f.readlines()

        # Cria o executor para processar os comandos
        executor = CommandExecutor()

        for linha in linhas:
            # Ignora linhas em branco ou comentários
            if linha.strip() == '' or linha.strip().startswith('--'):
                continue

            try:
                # Analisa e executa o comando da linha
                comando = parser.parse(linha.strip())
                if comando:
                    for cmd in comando:
                        resultado = executor.execute(cmd)
                        if resultado:
                            # Exibe os resultados, por exemplo, imprimindo as tabelas
                            if 'columns' in resultado and 'data' in resultado:
                                print(" | ".join(resultado['columns']))
                                for row in resultado['data']:
                                    print(" | ".join(str(x) for x in row))
            except Exception as e:
                print(f"Erro ao processar comando '{linha.strip()}': {e}")

def main():
    verificar_colunas()
    executor = CommandExecutor()
    # Processar o arquivo 'entrada.fca' se for fornecido como argumento
    if len(sys.argv) > 1:
        arquivo_entrada = sys.argv[1]
        processar_entrada_fca(arquivo_entrada)
    else:
                # Modo interativo
        while True:
            try:
                code = input("CQL> ")
                if code.lower() in ('exit', 'quit'):
                    break
                if code.lower().startswith('print table'):
                    table_name = code.split()[2]  # Extrai o nome da tabela
                    output = executor.execute(('PRINT', 'TABLE', table_name))
                    if output:
                        print(f"Tabela '{table_name}':")
                        print(output)
                    else:
                        print(f"Erro: Tabela '{table_name}' não encontrada")
                else:
                    result = parser.parse(code)
                    if result:
                        for command in result:
                            output = executor.execute(command)
                            if output:
                                print(" | ".join(output['columns']))
                                for row in output['data']:
                                    print(" | ".join(str(x) for x in row))
            except Exception as e:
                print(f"Erro: {e}")

if __name__ == "__main__":
    main()