class Arquivo:

    def __init__(self, arquivo=str):
        self.nlarquivo = arquivo
        try:
            open(self.nlarquivo)
        except FileNotFoundError:
            open(f'{self.nlarquivo}', 'w+')
        else:
            pass


    def ler(self):
        return open(f'{self.nlarquivo}', 'r')

    def escrever(self):
        return open(f'{self.nlarquivo}', 'a')

    def ler_escrever(self):
        return open(f'{self.nlarquivo}', 'a+')

    def ler_escrever_inicio(self):
        return open(f'{self.nlarquivo}', 'r+')

    def truncar(self):
        return open(f'{self.nlarquivo}', 'w')



def arquivoexiste(nome):
    """

    :param nome: Nome do arquivo
    :return: Retorna True se o arquivo existir, senao retorna False
    """
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    """

    :param nome: Nome do arquivo a ser criado
    :return: Sem retorno
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mOuve um erro na criação do arquivo!\033[m')


def lerarquivo(nome):
    """

    :param nome: Nome do arquivo a ser lido
    :return: Sem retorno
    """
    try:
        arqui = open(nome, 'r', encoding='utf-8')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        a = arqui.read()
        print('')
        print(a)
        print('')
        arqui.close()


def apagarlinha(nomearq='', numl=0):
    """

    :param nomearq: Nome do arquivo
    :param numl: Número da linha ser apagda
    :return: Sem Retorno
    """
    while True:
        try:
            with open(f'{nomearq}', 'r') as arq:
                linhasarqtemp = arq.readlines()
                if linhasarqtemp == []:
                    print('\033[31m -> Não a arquivos a serem removidos, a lista está vazia.\033[m')
                    break
                while numl < 0 or numl >= len(linhasarqtemp):
                    print('\033[31mERRO! A tarefa digitada não existe!!!\033[m')
                linhasarqtemp.remove(linhasarqtemp[numl])
                linhasarq = []
                for v in linhasarqtemp:
                    vl = ''
                    for nl, l in enumerate(v):
                        if nl > 3:
                            vl += f'{l}'
                    linhasarq.append(vl)
                with open(f'{nomearq}', 'w+') as arq:
                    for c, linha in enumerate(linhasarq):
                        arq.write(f'{linha}')
                    break
        except:
            print('\033[31m --> Um erro ocorreu <--')


def adicionarlinha(nomearq='', valoradd=''):
    """

    :param nomearq: Nome do arquivo
    :param valoradd: Valor a ser adicionado
    :return: Sem Retorno
    """
    with open(f'{nomearq}', 'r+', encoding='utf-8') as arq:
        arq.write(f'{valoradd}\n')

n = Arquivo('arqteste' ,'/home', 'doc', 'pdf')
print(n.tipo)
print(n.extensao)