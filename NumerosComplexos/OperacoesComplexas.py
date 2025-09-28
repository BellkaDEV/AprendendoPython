class complexNum:
    def __init__(self, parteReal, parteImag):
        self.parteReal = parteReal
        self.parteImag = parteImag

    def conjulgado(self):
        if self.parteImag == 0:
            return complexNum(self.parteReal, self.parteImag)
        elif self.parteImag != 0:
            return complexNum(self.parteReal, (-1)*self.parteImag)
        
    def printar(self):
        if self.parteImag != 0 and self.parteImag > 0:
            print(f"{round(self.parteReal, 2)}+{round(self.parteImag, 2)}i")
        elif self.parteImag != 0 and self.parteImag < 0:
            print(f"{round(self.parteReal, 2)}{round(self.parteImag, 2)}i")
        elif self.parteImag == 0:
            print(round(self.parteReal, 2))

    def soma(self, num2):
        return complexNum(
            self.parteReal + num2.parteReal,
            self.parteImag + num2.parteImag
        )
    
    def subtracao(self, num2):
        return complexNum(
            self.parteReal - num2.parteReal,
            self.parteImag - num2.parteImag
        )

    def multiplicacao(self, num2):
            return complexNum(
                (self.parteReal * num2.parteReal) + (self.parteImag * num2.parteImag * -1) , 
                (self.parteReal * num2.parteImag) + (self.parteImag * num2.parteReal)
                )
            
    
    def divisao(self, num2):
        conj = num2.conjulgado()
        numerador = self.multiplicacao(conj)
        denominador = num2.multiplicacao(conj)
        return complexNum(
        numerador.parteReal / denominador.parteReal,
        numerador.parteImag / denominador.parteReal
    )


    def mirrow(self) :
        return complexNum(self.parteReal, self.parteImag)

def menu() :
    print("1. Potencias de i.")
    print("2. Operações com i.")
    print("3. Sair")

def menu2() :
    print("1. Soma.")
    print("2. Subtração.")
    print("3. Multiplicação.")
    print("4. Divisão.")
    print("5. Voltar.")

def potenciaI(p):
    if p % 4 == 0:
        return "1"
    elif p % 4 == 1:
        return "i"
    elif p % 4 == 1:
        return "-1"
    elif p % 4 == 1:
        return "-i"
    
if __name__ == "__main__":

    n1 = complexNum(3, 4)
    n2 = complexNum(2, -1)

    
    n1.printar()
    n2.printar()
    n3 = n1.divisao(n2)
    n3.printar()