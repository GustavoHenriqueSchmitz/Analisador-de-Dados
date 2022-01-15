def cadentrar(documento=''):
    """

    :param documento: Documento onde conterá as insformações de login
    :return: Retorna o nome e a senha
    """
    #Programa Principal
    print('-' * 40)
    print(f'{"ENTRAR":^40}')
    print('-' * 40)
    while True:
        try:
            arq = open(documento, 'r')
        except:
            print('\033[31mERRO! Ao abrir o arquivo\033[m')
        while True:
            arq.seek(0)
            nome = str(input('\033[35mUsuário: '))
            senha = str(input('Senha: \033[m'))
            if f'{nome}\n' in arq and f'{senha}\n' in arq:
                break
            else:
                print('\033[31m!Usuário ou Senha inválidos!\033[m')
        return nome, senha

def cadastrar(documento=''):
    # Funções/Módulos Importados
    from random import choice, randint

    #Programa Principal
    print('-' * 40)
    print(f'{"CADASTRAR":^40}')
    print('-' * 40)
    while True:
        try:
            arq = open(documento, 'a')
        except:
            print('\033[31mERRO! Ao abrir o arquivo\033[m')
        while True:
            n = str(input('\033[35mNome de usuário: '))
            s = str(input('Sua senha[Digite [G] para utilizar o gerador de senhas]: \033[m'))
            print('-' * 40)
            if s == 'G' or s == 'g':
                s = ''
                letrasnum = ['4', 'a', 'b', '1', 'c', '0', 'd', 'e', '2', '2', 'f', '3', 'g', 'h', '6', 'i', 'j', 'k',
                            '3', 'l', 'm', '4', 'n', '5', 'o', 'p',
                             'q', '6', '9', '7', 'r', 's', '8', 't', '9', '8', 'u', 'v', '7', 'w', 'x', 'y', 'z', '1',
                             '5', '0']
                while True:
                    try:
                        caracteres = int(input('\033[36mQuantos caracteres a senha térá?\033[m'))
                    except:
                        print('\033[31mERRO! Digite um valor númerico!!!\033[m')
                        continue
                    break
                while True:
                    try:
                        tipo = int(input(''' \033[32m<> FORMATO DA SENHA <> \033[33m\n1 - \033[34mSomente números\n\033[33m2 - \033[34mSomente letras\033[33m\n\033[33m3 -\033[34m Letras e números\n\033[34mR:\033[m'''))
                    except:
                        print('\033[31mERRO! Opção ínvalida\033[m')
                        continue
                    break
                if tipo == 1:
                    for v in range(0, caracteres):
                        num = randint(0, 9)
                        s += f'{num}'
                elif tipo == 2:
                    print('''\033[33m2.1 -\033[34m Para letras maiúsculas\033[m\n\033[33m2.2 -\033[34m Para letras minúsculas\033[m''')
                    tipo2 = str(input('\033[33mR:\033[m '))
                    while tipo2 != '2.1' and tipo2 != '2.2':
                        print(' \033[31m!> Valores digitados inválidos <!\033[m')
                        tipo2 = str(input('\033[33mR:\033[m '))
                    if tipo2 == '2.1':
                        for v in range(0, caracteres):
                            let = choice(letrasnum)
                            while let.isnumeric():
                                let = choice(letrasnum)
                            s += f'{let}'
                    elif tipo2 == '2.2':
                        for v in range(0, caracteres):
                            let = choice(letrasnum)
                            while let.isnumeric():
                                let = choice(letrasnum)
                            s += f'{let}'
                elif tipo == 3:
                    print('''\033[33m2.1 -\033[34m Para letras maiúsculas\033[m\n\033[33m2.2 -\033[34m Para letras minúsculas\033[m''')
                    tipo2 = str(input('\033[33mR:\033[m '))
                    while tipo2 != '2.1' and tipo2 != '2.2':
                        print(' \033[31m!> Valores digitados inválidos <!\033[m')
                        tipo2 = str(input('\033[33mR:\033[m '))
                    if tipo2 == '2.1':
                        for v in range(0, caracteres):
                            nl = choice(letrasnum)
                            s  += f'{nl}'
                    elif tipo2 == '2.2':
                        for v in range(0, caracteres):
                            nl = choice(letrasnum)
                            s += f'{nl}'
            print('-' * 40)
            print(f'\033[33mNome de Usuário ->\033[34m {n}\033[m')
            print(f'\033[33mSua senha ->\033[34m {s}\033[m')
            print('-' * 40)
            r = str(input('\033[35mCadastrar \033[35m[S/N]: \033[m')).strip().upper()
            print('-' * 40)
            if r == 'S':
                arq.write(f'{n}\n')
                arq.write(f'{s}\n')
                arq.close()
                break
            else:
                continue
        break
