from ferramentas import interface
import pandas as pd
from IPython.display import display
from os.path import splitext

quebra_while = 0

while True:
    interface.cabecalho('Analisador de Dados')
    print("""|Para começar sua analise.
|vamos definir o tipo da tabela.
|Ex: Excel, csv.
|E após isso importa-la.
----------------------------------------""")
    while True:

        if quebra_while > 0:
            quebra_while -= 1
            break

        try:
            tipo = str(input('Tipo de tabela: ')).lower().strip()
            print('----------------------------------------')
            pdcd = f'read_{tipo}'
            pdcd = getattr(pd, pdcd)

        except:
            print('O tipo de tabela definido, não existe. Ou não é suportado.')
            print('----------------------------------------')

        else:

            while True:

                if quebra_while > 0:
                    quebra_while -= 1
                    break

                try:
                    tabela = str(input('Tabela a ser analisada: '))
                    print('----------------------------------------')
                    tabela = pdcd(tabela)

                except FileNotFoundError:
                    print('O arquivo especificado, não foi encontrado.')
                    continue

                except ValueError:
                    arquivo, extensao = splitext(f'{tabela}')
                    print(f"""O arquivo: {arquivo}\né do tipo {extensao} e não {tipo} como definido anteriormente.
                    """)
                    rtipo = str(input(f'Deseja abrir o arquivo como {extensao}[s/n]? ')).lower().strip()

                    if rtipo == 's':
                        tipo = extensao.replace('.', '')
                        pdcd = f'read_{tipo}'
                        pdcd = getattr(pd, pdcd)
                        tabela = pdcd(tabela)
                        break

                    elif rtipo == 'n':
                        quebra_while += 1
                        break

                else:
                    break

            while True:

                if quebra_while > 0:
                    quebra_while -= 1
                    break

                print('----------------------------------------')
                display(tabela)
                print('----------------------------------------')
                break

