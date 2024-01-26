def __init__(self, numero, fecha, titular, saldo):
        self.__numero = numero
        self.__fecha = fecha
        self.__titular = titular
        self.__saldo = saldo

        @property
        def numero(self):
            return self.__numero
   
        @numero.setter
        def numero(self, valor):
            self.__numero = valor
   
        @property
        def fecha(self):
            return self.__fecha
   
        @fecha.setter
        def fecha(self, valor):
            self.__fecha = valor
       
        @property
        def titular(self):
            return self.__titular
   
        @titular.setter
        def titular(self, valor):
            self.__titular = valor
       
        @property
        def saldo(self):
            return self.__saldo
   
        @saldo.setter
        def saldo(self, valor):
            self.__saldo = valor

        def descontarSaldo(self, valor):
            self.__saldo = self.__saldo - valor
            return self.__saldo

        def __str__(self):
            return 'Nombre:' + self.__titular + ' caduca en: ' + self.__fecha + ' y tiene: ' + str(self.__saldo) + ' €'



tarjeta1 = tarjeta1(1,'10/26','Santi',1000)

tarjeta1.fecha = '12/27'
print(tarjeta1.descontarSaldo(200))

print(tarjeta1)