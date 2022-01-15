from ferramentas import interface
from ferramentas import cores
import pandas as pd
from IPython.display import display
from os.path import splitext

quebra_while = 0

while True:

    if quebra_while > 0:
        quebra_while -= 1
        break

    interface.cabecalho('Analisador de Dados')
    print(f"""|Para começar sua analise.
|vamos definir o tipo da tabela.
|Ex: Excel, csv.
|E após isso importa-la.""")
    interface.linha(50)
    while True:

        if quebra_while > 0:
            quebra_while -= 1
            break

        try:
            tipo = str(input('Tipo de tabela: ')).lower().strip()
            interface.linha(50)
            pdcd = f'read_{tipo}'
            pdcd = getattr(pd, pdcd)

        except:
            print('O tipo de tabela definido, não existe. Ou não é suportado.')
            interface.linha(50)

        else:

            while True:

                if quebra_while > 0:
                    quebra_while -= 1
                    break

                try:
                    tabela = str(input('Tabela a ser analisada: '))
                    interface.linha(50)
                    tabela = pdcd(tabela)

                except FileNotFoundError:
                    print('O arquivo especificado, não foi encontrado.')
                    continue

                except ValueError:
                    arquivo, extensao = splitext(f'{tabela}')
                    print(f"""O arquivo: {arquivo}\né do tipo {extensao} e não {tipo}, como definido anteriormente.\n{interface.linha(40)}""")
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

            interface.linha(50)
            display(tabela)
            interface.linha(50)
            while True:

                if quebra_while > 0:
                    quebra_while -= 1
                    break

                op = interface.menu(['Ver tabela', 'Ver informações da tabela', 'Tratamento de dados', 'Análise Inicial', 'Analise Detalhada', 'Exportar Tabela', 'Exportar Gráficos', 'Importar outra tabela', 'Configurações', 'Ajuda', 'Finalizar Programa'])
                interface.linha(50)
                if op == 1:
                    display(tabela)

                elif op == 2:
                    display(tabela.info())

                elif op == 8:
                    quebra_while = 1
                    continue

                elif op == 11:
                    quebra_while = 4
                    print('Finalizando o Programa!')
                    continue

                else:
                    print(f'{cores.vermelho()}Em desenvolvimento.{cores.retirarcor()}')
                    continue
