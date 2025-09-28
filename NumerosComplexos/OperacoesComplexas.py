import os
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
    print("5. Conjulgado dos numeros.")
    print("6. Voltar.")

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

    opc = 0
    opc1 = 0
    
while opc != 3:
    menu()
    opc = int(input("Digite sua escolha: "))
    match opc:
        case 1:
            p = input("Digite a potecia de i: ")
            print(f"O valor final de i é igual a: {potenciaI(p)}")
        case 2:
            while opc1 != 6:
                a = input("Digite a parte Real do primeiro numero complexo: ")
                b = input("Digite a parte Imaginaria do primeiro numero complexo: ")
                n1 = complexNum(a, b)

                a = input("Digite a parte Real do segundo numero complexo: ")
                b = input("Digite a parte Imaginaria do segundo numero complexo: ")
                n2 = complexNum(a, b)

                menu2()
                opc1 = int(input("Oque pretende fazer com esses dois numeros? \nDigite sua escolha: "))
                match opc1:
                    case 1:
                        print(f"A soma dos dois numeros complexos é: {n1.soma(n2)}")
                    case 2:
                        print(f"A subtração dos dois numeros complexos é: {n1.subtracao(n2)}")
                    case 3:
                        print(f"A multiplicação dos dois numeros complexos é: {n1.multiplicacao(n2)}")
                    case 4:
                        print(f"A divisão dos dois numeros complexos é: {n1.divisao(n2)}")
                    case 5:
                        print(f"OS conjulgadoS dos dois numeros são: \n{n1.printar()} --> {(n1.conjulgado()).printar()}\n{n2.printar()} --> {(n2.conjulgado()).printar()}")
                    case 6:
                        break
                    case _:
                        print("Opção inválida")
                    
        case 3: 
            print("Saindo...")
            break
        case _:
            print("Opção inválida")
os.system("clear")