def aumentar(preco=0, taxa=0, formato=False):
    """

    :param preco: Preço do produto ou objeto
    :param taxa: Taxa% de aumento
    :param formato: Define se será formatado (True) ou não (False)
    :return: Retorna o valor com o aumento somado
    """
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    """

    :param preco: Preço do produto ou objeto
    :param taxa: Taxa% de diminuição
    :param formato: Define se será formatado (True) ou não (False)
    :return: Retorna o valor já subtraído
    """
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    """

    :param preco: Preço do produto ou objeto a ser dobrado
    :param formato: Define se será formatado (True) ou não (False)
    :return: Retorna o valor dobrado
    """
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    """

    :param preco: Preço do produto ou objeto
    :param formato: Define se será formatado (True) ou (False)
    :return: Retorna o valor pela metade
    """
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    """

    :param preco:O valor/preço de um produto ou objeto
    :param moeda: Tipo de moeda
    :return: Retorna o preço formatado.
    """
    return (f'{moeda}{preco:>.2f}'.replace('.', ',')) if moeda == 'R$' else (f'{moeda}{preco:>.2f}'.replace(',', '.'))


def leiadinheiro(num):
    """

    :param num: Texto que será mostrado no input
    :return:Retorna o valor formatado como dinheiro
    """
    ndef = str(input(num)).strip()
    if ndef.replace('.', '').isnumeric() or ndef.replace(',', '').isnumeric():
        return float(ndef.replace(',', '.'))
    while True:
        print(f'\033[31mERRO: "{ndef}" é um preço inválido!\033[m')
        ndef = str(input(num)).strip()
        if ndef.replace('.', '').isnumeric() or ndef.replace(',', '').isnumeric():
            return float(ndef.replace(',', '.'))
