def lerarquivo(nome):
    """

    :param nome: Nome do arquivo a ser lido
    :return:Ser um retorno
    """
    try:
        arqui = open(nome, 'r')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        a = arqui.read()
        print('')
        print(a)
        print('')
        arqui.close()


def leiaint(msg):
    """

    :param msg: Texto a ser mostrado no input
    :return:Retorna o valor int(inteiro)
    """
    while True:
        try:
            nintl = int(input(msg))
        except (TypeError, ValueError):
            print(f'\033[31mO valor digitado não é inteiro.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados encerrada pelo usuário\033[m')
            return 0
        else:
            return nintl


def leianumbin(numbin):
    """

    :param numbin: Texto a ser mostrado no input
    :return: Retorna o valor binário
    """
    cont = 0
    while True:
        bin = str(input(numbin)).strip().upper()
        for v in bin:
            if v != '0' and v != '1' and v != 'Q':
                cont += 1
        if cont > 0:
            print('\033[31m>>> O VALOR DIGITADO NÃO É BINÁRIO !!!\033[m')
            cont = 0
        return bin


def leiadinheiro(num):
    """

    :param num: Texto a ser mostrado no input
    :return: Retorna o valor na forma monetária
    """
    ndef = str(input(num)).strip()
    if ndef.replace('.', '').isnumeric() or ndef.replace(',', '').isnumeric():
        return float(ndef.replace(',', '.'))
    while True:
        print(f'\033[31mERRO: "{ndef}" é um preço inválido!\033[m')
        ndef = str(input(num)).strip()
        if ndef.replace('.', '').isnumeric() or ndef.replace(',', '').isnumeric():
            return float(ndef.replace(',', '.'))


def leiafloat(msg):
    """

    :param msg: Texto a ser mostrado no input
    :return: Retorna um valor real
    """
    while True:
        try:
            nfloatl = float(input(msg))
        except (TypeError, ValueError):
            print(f'\033[31mO valor digitado não é Real.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados encerrada pelo usuário\033[m')
            return 0
        else:
            return nfloatl


def leiaresposta(txt='', numresp=1):
    """

    :param txt: Texto a ser mostrado no input
    :param numresp: Número possivel de respostas
    :return: Retorna a resposta
    """
    while True:
        try:
            resp = int(input(txt))
        except:
            print('\033[31mERRO! Resposta invalida\033[m')
        else:
            if resp > numresp or resp <= 0:
                print('\033[31mERRO! Resposta invalida\033[m')
                continue
            else:
                return resp

def leiarespostaSN(txt='', minmai='mai'):
    """

    :param txt: Texto a ser mostrado no input
    :param minmai: Se a resposta será retornada como maiúscula ou minúscula
    :return: Retorna um valor S (SIM) ou N (NÃO)
    """
    while True:
        r = str(input(txt))
        if minmai == 'mai':
            if r not in 'S' and r not in 's' and r not in 'n' and r not in 'N':
                print('\033[31mERRO! Digite um valor valído [S/N]..\033[m')
                continue
            r = r.upper()
            if r == 'S' or 'N':
                return r
        if minmai == 'min':
            if r not in 'S' or r not in 's' or r not in 'n' or r not in 'N':
                print('\033[31mERRO! Digite um valor valído [S/N]..\033[m')
                continue
            r = r.lower()
            if r == 's' or 'n':
                return r
