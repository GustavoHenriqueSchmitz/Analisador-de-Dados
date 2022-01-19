class cores:

    @staticmethod
    def preto():
        return '\0331;30m'

    @staticmethod
    def vermelho():
        return '\033[1;31m'

    @staticmethod
    def verde():
        return '\033[1;32m'

    @staticmethod
    def amarelo():
        return '\033[1;33m'

    @staticmethod
    def azul():
        return '\033[1;34m'

    @staticmethod
    def magenta():
        return '\033[1;35m'

    @staticmethod
    def ciano():
        return '\033[1;36m'

    @staticmethod
    def cinzaclaro():
        return '\033[1;37m'

    @staticmethod
    def cinzaescuro():
        return '\033[1;90m'

    @staticmethod
    def vermelhoclaro():
        return '\033[1;91m'

    @staticmethod
    def verdeclaro():
        return '\033[1;92m'

    @staticmethod
    def amareloclaro():
        return '\033[1;93m'

    @staticmethod
    def azulclaro():
        return '\033[1;94m'

    @staticmethod
    def magentaclaro():
        return '\033[1;95m'

    @staticmethod
    def cianoclaro():
        return '\033[1;96m'

    @staticmethod
    def branco():
        return '\033[1;97m'

    @staticmethod
    def retirarcor():
        return '\033[m'

def tradutor_de_cores(cor):

    if cor == 'vermelho':
        return 'red'

    elif cor == 'amarelo':
        return 'yellow'

    elif cor == 'azul':
        return 'blue'

    elif cor == 'laranja':
        return 'orange'

    elif cor == 'verde':
        return 'green'

    elif cor == 'roxo':
        return 'purple'

    elif cor == 'marrom':
        return 'brown'

    elif cor == 'preto':
        return 'black'