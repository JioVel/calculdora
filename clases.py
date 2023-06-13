class Calculadora():
    def init(self, numero):
        self.acumulado = numero

    def suma(self, numero):
        self.acumulado += numero

    def resta(self, numero):
        self.acumulado -= numero


    def multiplicacion(self, numero):
        self.acumulado = self.acumulado * numero

    def division(self, numero):
        self.acumulado = self.acumulado / numero

    def reiniciar(self):
        self.acumulado =0