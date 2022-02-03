#Módulos/Bibliotecas Utilizados
from ferramentas import interface
from ferramentas import cores
import pandas as pd
from IPython.display import display
from os.path import splitext
from ferramentas import leia
import plotly.express as px

#Quantia de loopings while, a serem quebrados. A utilidade desa variavel, é quebrar mais de 1 looping while, de uma vez.
quebra_while = 0

#Ínicio do programa
while True:
    #Verifica se o looping while atual, deve ser quebrado em sequência de outro.
    if quebra_while > 0:
        quebra_while -= 1
        break
    interface.cabecalho('Analisador de Dados')
    print(f'| Para começar sua analise,        |')
    print(f'| Basta importar a tabela.         |')
    interface.linha(50)

    #inicia a importação.
    while True:

        # Verifica se o looping while atual, deve ser quebrado em sequência de outro.
        if quebra_while > 0:
            quebra_while -= 1
            break

        #Localizando a tabela a ser aberta.
        try:
            print('Digite [esc], para cancelar.')
            interface.linha(50)
            tabela_nome = str(input('Tabela a ser analisada: '))

            # Permite o usuário cancelar a etapa.
            if tabela_nome.lower() == 'esc':
                break

            #Abre a tabela
            arquivo, extensao = splitext(f'{tabela_nome}')
            comando = f'read_{extensao.replace(".", "")}'
            comando = getattr(pd, comando)
            interface.linha(50)
            tabela = comando(tabela_nome)

        #Verifica os erros.
        except FileNotFoundError:
            print('O arquivo especificado, não foi encontrado.')
            interface.linha(50)
            continue

        except:
            interface.linha(50)
            print('Houve algum erro, ao abrir tabela.')
            continue

        #Após tudo, ele abre a tabela escolhida para visualização.
        interface.linha(50)
        display(tabela)
        interface.linha(50)
        #Em seguida abrindo o menu de Análise da tabela.
        while True:

            # Verifica se o looping while atual, deve ser quebrado em sequência de outro.
            if quebra_while > 0:
                quebra_while -= 1
                break

            #Menu de análise
            op = interface.menu(['Ver tabela', 'Ver informações da tabela', 'Tratamento de dados', 'Análise', 'Exportar Tabela', 'Restaurar tabela', 'Importar outra tabela', 'Configurações', 'Ajuda', 'Finalizar Programa'])
            interface.linha(50)

            #Opção 1, para mostrar a tabela.
            if op == 1:
                display(tabela)

            #Opção 2, para visualizar informações da tabela.
            elif op == 2:
                display(tabela.info())

            #Opção 3, cujo objetivo, é tratar os dados da tabela
            elif op == 3:

                #Menu de tratamento de dados
                while True:
                    op = interface.menu(['Ver tabela', 'Ver informações da tabela', 'Apagar coluna', 'Apagar linha', 'Mudar Dtype de uma coluna -> int/float', 'Voltar ao menu'], titulo='Tratamento de Dados')

                    #Opção 1, para mostrar a tabela.
                    if op == 1:
                        display(tabela)

                    #Opção2, para visualizar informações da tabela
                    elif op == 2:
                        display(tabela.info())

                    #Opção 3, apagar colunas.
                    elif op == 3:

                        while True:
                            op = interface.menu(['Apagar coluna', 'Apagar colunas, com qualquer valor vazio', 'Apagar colunas, com todos os valores vazios', 'Voltar'], titulo='Apagar Coluna')

                            #Opção 1, permite apagar uma coluna específica
                            if op == 1:

                                    try:
                                        interface.linha(50)
                                        print('Digite [esc], para cancelar.')
                                        interface.linha(50)
                                        nome_coluna = str(input('Digite o nome da coluna a ser apagada: '))

                                        # Permite o usuário cancelar a etapa.
                                        if nome_coluna.lower() == 'esc':
                                            continue

                                        tabela = tabela.drop(nome_coluna, axis=1)

                                    except KeyError:
                                        print('A coluna digitada, não existe.')
                                        continue

                                    except:
                                        print('Houve algum erro, ao apagar a coluna.')

                                    else:
                                        continue

                            #Opção 2, exclui colunas, com qualquer valor vazio.
                            elif op == 2:

                                try:
                                    tabela = tabela.dropna(how='any', axis=1)

                                except:
                                    print('Ouve um erro, ao apagar as colunas.')
                                    continue

                            #Opção 3, exclui colunas, com todos os seus valores vazios.
                            elif op == 3:

                                try:
                                    tabela = tabela.dropna(how='all', axis=1)

                                except:
                                    print('Ouve um erro, ao apagar as colunas.')
                                    continue


                            #opção 4, Volta ao menu anterior.
                            elif op == 4:
                                break

                    #Apagar linhas.
                    elif op == 4:

                        while True:
                            op = interface.menu(['Apagar linha', 'Apagar linhas, com qualquer valor vazio', 'Apagar linhas, com todos os valores vazios', 'Voltar'], titulo='Apagar Linhas')

                            #Permite o usuário apagar uma linha especifíca.
                            if op == 1:
                                try:
                                    interface.linha(50)
                                    print('Digite [esc], para cancelar.')
                                    interface.linha(50)
                                    num_linha = str(input('Digite o número da linha a ser apagada: '))

                                    # Permite o usuário cancelar a etapa.
                                    if num_linha == 'esc':
                                        continue

                                    tabela = tabela.drop(int(num_linha), axis=0)

                                except KeyError:
                                    print('A linha digitada, não existe.')
                                    continue

                                except:
                                    print('Houve algum erro, ao apagar a linha.')

                                else:
                                    continue

                            # Opção 2, exclui linhas, com qualquer valor vazio.
                            elif op == 2:

                                try:
                                    tabela = tabela.dropna(how='any', axis=0)

                                except:
                                    print('Ouve um erro, ao apagar as linhas.')
                                    continue

                            # Opção 3, exclui linhas, com todos os seus valores vazios.
                            elif op == 3:

                                try:
                                    tabela = tabela.dropna(how='all', axis=0)

                                except:
                                    print('Ouve um erro, ao apagar as linhas.')
                                    continue

                            elif op == 4:
                                break
                    #Permite o usuário, mudar o Dtype de uma coluna, para númérico.
                    elif op == 5:

                        try:
                            print('Digite [esc], para cancelar.')
                            coluna = str(input('Digite o nome da coluna: '))

                            if coluna == 'esc':
                                continue

                            tabela[coluna] = pd.to_numeric(tabela[coluna], errors="coerce")

                        except KeyError:
                            print('A coluna digitada, não existe.')
                            continue

                        except:
                            print('Ouve um erro, ao mudar o Dtype.')

                    #Opção 6, Volta ao menu principal.
                    elif op == 6:
                        break

            elif op == 4:

                while True:
                    op = interface.menu(['Análise Gráfica', 'Análise Informativa', 'Voltar ao Menu'], titulo="Análise")

                    if op == 1:
                        tipo_grafico = 'histogram'
                        cores_grafico = 'padrao'
                        tipo_analise = 'None'
                        coluna1 = 'None'
                        coluna2 = 'None'

                        while True:
                            op = interface.menu(['Executar análise', 'Visualizar gráficos', 'Visualizar Configurações', 'Configurar análise', 'Voltar'], titulo="Análise Gráfica")

                            if op == 1:
                                pass

                            elif op == 3:
                                interface.linha(50)
                                print(f'Tipo_Gráfico = {tipo_grafico}')
                                print(f'Cores = {cores_grafico}')
                                print(f'Tipo_Análise = {tipo_analise}')
                                print(f'Coluna 1 = {coluna1}')
                                print(f'Coluna 2 = {coluna2}')

                            elif op == 4:
                                while True:
                                    op = interface.menu(['Tipo_Gráfico', 'Cores', 'Tipo_Análise', 'Coluna 1', 'Coluna 2', 'Terminar de Configurar'], titulo="Configurações")

                                    if op == 1:
                                        op = interface.menu(['Histogram', 'Line', 'Area', 'Bar', 'Timeline', 'ecdf', 'strip', 'pie', 'parallel_coordinates', 'Voltar'], titulo="Tipo_Gráfico", retorna='str')
                                        tipo_grafico = op

                                    elif op == 2:
                                        interface.opcoes(['Padrão', 'Vermelho', 'Amarelo', 'Azul', 'Laranja', 'Verde', 'Roxo', 'Marrom', 'Preto', 'Terminar de configurar'], titulo="Cores")
                                        cont = 0
                                        while True:
                                            cont += 1
                                            interface.linha(50)
                                            print(f' -> Cor {cont}')
                                            op = interface.menu(['padrao', 'vermelho', 'amarelo', 'azul', 'laranja', 'verde', 'roxo','marrom', 'preto', 'terminar de configurar'], mostrar_op='False', titulo="Cores", retorna="stint")

                                            if op[0] == 10:
                                                break

                                            elif op[0] == 1:
                                                cores_grafico = 'padrao'
                                                print('Definido como Padrão')
                                                break

                                            if cont == 1:
                                                cores_grafico = []

                                            print(cores_grafico)
                                            cores_grafico.append(op[1])

                                    elif op == 3:
                                        interface.opcoes(['Gráfico único -> Compara a coluna 1, com a coluna 2.', 'Toda a tabela -> Compara a coluna 1, com todas as colunas da tabela.'], titulo="Tipo da Análise")
                                        op = interface.menu(['grafico unico', 'toda a tabela'], mostrar_op=False, retorna="str")
                                        tipo_analise = op

                                    elif op == 4:
                                        coluna1 = str(input('Coluna 1: '))

                                    elif op == 5:
                                        coluna2 = str(input('Coluna 2: '))

                                    elif op == 6:
                                        break


                            elif op == 5:
                                break

                    elif op == 3:
                        break

            #A opção 6, restaura o estado da tabela
            elif op == 6:
                try:
                    tabela = comando(tabela_nome)
                except:
                    print('Ouve um erro, ao restaurar a tabela.')

            #Fecha o programa
            elif op == 10:
                print('Finalizando o Programa!')
                exit()

            else:
                print(f'{cores.cores.vermelho()}Em desenvolvimento.{cores.cores.retirarcor()}')
                continue
