
def linha(var=0):
    """

    :param var: Tamanho da linha ou variavel, na qual será contabilizada a aquntia de caracteres dessa variavel e montada a linha
    :return: Retorna a linha ou melhor escreve uma linha
    """
    var = str(var)
    if var.isnumeric():
        var = int(var)
        if var >= 0:
            return print('-' * var)
    else:
        lenvar = len(var) + 3
        return print('-' * lenvar)


def cabecalho(titulo=''):
    """

    :param txt: Texto do cabeçalho
    :return: Sem retorno
    """
    print('-' * 50)
    print(titulo.center(50))
    print('-' * 50)


def menu(lista, cor1='\033[m', cor2='\033[m', titulo='Menu', retorna='int'):
    """

    :param lista: Lista onde deverá ser digitado as opções do menu
    :param cor1: Primeira cor do menu, deve ser definida por código ANSI ou seja \033[
    -> https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/
    :param cor2: Segunda Cor do menu, deve ser definida por código ANSI ou seja \033[
    -> https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/
    :param titulo: Título do menu
    :return: Se o parâmetro retorna ser int(inteiro) ele retorna o número da opção escolhida | Se o parâmetro
    ser str(string) ele retorna os caracteres da opção | se o parâmetro ser stint ele retornará tanto o número da opção tanto os caracteres

    Por exemplo

    1 - Opção 1
    2 - Opção 2
    3 - opção 3

    Escolhendo int, ele reotornaria os valores 1,2,3.
    Escolhendo str, ele reotornaria os caracteres Opção 1, Opção 2, Opção 3.
    Escolhendo stint, ele reornaria tanto 1,2,3 tanto opção 1, opção 2, opção 3 os dois tipos
    em uma lista.
    """
    print('-' * 50)
    print(f'{titulo:^50}')
    print('-' * 50)
    for c, item in enumerate(lista):
        print(f'{cor1}{c + 1} - {cor2}{item}\033[m')
    print('-' * 50)
    while True:
        try:
            opc = int(input(f'{cor1}Opção:\033[m '))
        except:
            print('\033[31m!!!ERRO!Digite uma opção numérica!!!\033[m')
            continue
        if opc > len(lista) or opc < 1:
            print('\033[31m!!!ERRO! Digite uma opção Valida!!!\033[m')
            continue
        else:
            if retorna.lower().strip() == 'int':
                return opc
            elif retorna.lower().strip() == 'str':
                return lista[opc - 1]
            elif retorna.lower().strip() == 'stint':
                return opc, lista[opc - 1]
