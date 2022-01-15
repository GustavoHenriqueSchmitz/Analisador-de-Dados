import datetime
import calendar

class RetornaData:

    def __init__(self, ano=datetime.date.today().strftime('%Y'), mes=datetime.date.today().strftime('%m'), dia=datetime.date.today().strftime('%d'), hora=datetime.datetime.now().strftime('%H'), min=datetime.datetime.now().strftime('%M'), seg=datetime.datetime.now().strftime('%S')):
        """

        :param ano: Digite o ano desejado ou nada para obter o ano atual
        :param mes: Digite o mês desejado ou nada para obter o mês atual
        :param dia: Digite o dia desejado ou nada para obter o dia atual
        :param hora: Digite a hora desejada ou nada para obter a hora atual
        :param min: Digite o minuto desejado ou nada para obter o minuto atual
        :param seg: Digite o segundo desejado ou nada para obter o segundo atual
        """

        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.hora = hora
        self.min = min
        self.seg = seg
        self.__datahorajun = f'{self.ano}-{self.mes}-{self.dia} {self.hora}:{self.min}:{self.seg}'
        self.__datahorasep = {'ano': f'{self.ano}', 'mes': f'{self.mes}', 'dia': f'{self.dia}', 'hora': f'{self.hora}', 'minuto': f'{self.min}', 'segundo': f'{self.seg}'}

    def retorna_data_hora_sep(self):
        """

        Esse método funiona em relaçã ao objeto criado

        :return: Retorna um dicionário com a data separada por ano, mês, dia...
        """
        return self.__datahorasep

    def retorna_data_hora_jun(self):
        """

        Esse método funciona em relação ao objeto criado

        :return: Retorna a data tudo junto formatada e ajustada, em modo string
        """
        return self.__datahorajun

    def retorna_tipo_especifico(self, tipodata=0):
        """

        Esse método funciona em relação ao objeto criado

        :param tipodata: Digite o tipo da data a ser retornada
        Digite:
        1 -> Para retornar o ano
        2 -> Para retornar o mês
        3 -> Para retornar o dia
        4 -> Para retornar a hora
        5 -> Para retornar o minuto
        6 -> Para retornar o segundo

        :return: Retorna o tipo selecionado
        """
        if tipodata == 1:
            return self.__datahorasep['ano']
        elif tipodata == 2:
            return self.__datahorasep['mes']
        elif tipodata == 3:
            return self.__datahorasep['dia']
        elif tipodata == 4:
            return self.__datahorasep['hora']
        elif tipodata == 5:
            return self.__datahorasep['minuto']
        elif tipodata == 6:
            return self.__datahorasep['segundo']
        else:
            print(f'\033[31mO tipo digitado é invalido:\033[1;31m\n'
                  f'Digite\n'
                  f'\033[32m -> 1 Para retornar o ano\n'
                  f'\033[32m -> 2 Para retornar o mês\n'
                  f'\033[32m -> 3 Para retornar o dia\n'
                  f'\033[32m -> 4 Para retornar a hora\n'
                  f'\033[32m -> 5 Para retornar o minuto\n'
                  f'\033[32m -> 6 Para retornar o segundo\n\033[m')

    @staticmethod
    def retorna_dias_mes(ano, mes):
        """

        :param ano: Indicar o ano
        :param mes: Indicar o mês no qual serão calculados os dias
        :return: Retorna a quantia de dias que o mês possui
        """
        mesrange = calendar.monthrange(ano, mes)
        return mesrange[1]
