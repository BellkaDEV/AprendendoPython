import os
import math

class complexNum:
    def _init_(self, parteReal, parteImag):
        self.parteReal = parteReal
        self.parteImag = parteImag

    def conjulgado(self):
        if self.parteImag == 0:
            return complexNum(self.parteReal, self.parteImag)
        elif self.parteImag != 0:
            return complexNum(self.parteReal, (-1)*self.parteImag)
        
    def printar(self):
        real = round(self.parteReal)
        imag = round(self.parteImag)
        if imag == 0:
            return str(real)
        elif real == 0:
            if imag == 1:
                return "i"
            elif imag == -1:
                return "-i"
            else:
                return f"{imag}i"
        else:
            if imag > 0:
                if imag == 1:
                    return f"{real}+i"
                else: 
                    return f"{real}+{imag}i"
            else:
                if imag == -1:
                    return f"{real}-i"
                else:
                    return f"{real}{imag}i"

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

    def forma_polar(self):
        modulo = math.hypot(self.parteReal, self.parteImag)
        argumento_rad = math.atan2(self.parteImag, self.parteReal)
        argumento_deg = math.degrees(argumento_rad)
        
        print("\n-------------------------------------------")
        print(f"Número Complexo: {self.printar()}")
        print("-------------------------------------------")
        print(f"Módulo (r): {modulo:.4f}")
        print(f"Argumento (θ) em Radianos: {argumento_rad:.4f} rad")
        print(f"Argumento (θ) em Graus: {argumento_deg:.4f}°")
        print("\nFórmula Polar (Forma Trigonométrica):")
        print(f"z = {modulo:.4f} * (cos({argumento_deg:.4f}°) + i * sin({argumento_deg:.4f}°))")
        print("-------------------------------------------\n")

    def mirrow(self) :
        return complexNum(self.parteReal, self.parteImag)

def invalido(opc):
    if (opc != 1) and (opc != 2) and (opc != 3) and (opc != 4) and (opc != 5) and (opc != 6):
        return True

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
    print("6. Forma Polar.")
    print("7. Voltar.")

def potenciaI(p):
    if p % 4 == 0:
        return "1"
    elif p % 4 == 1:
        return "i"
    elif p % 4 == 1:
        return "-1"
    elif p % 4 == 1:
        return "-i"
    
if _name_ == "_main_":

    opc = 0
    opc1 = 0
    
while opc != 3:
    opc1 = 0
    opc = 0
    menu()
    opc = int(input("Digite sua escolha: "))
    match opc:
        case 1:
            p = int(input("Digite a potecia de i: "))
            print(f"O valor final de i é igual a: {potenciaI(p)}")
        case 2:
            while opc1 != 7:
                menu2()
                opc1 = int(input("Oque pretende fazer com esses dois numeros? \nDigite sua escolha: "))
        
                if not invalido(opc1):
                    a = float(input("Digite a parte Real do primeiro numero complexo: "))
                    b = float(input("Digite a parte Imaginaria do primeiro numero complexo: "))
                    n1 = complexNum(a, b)

                    a = float(input("Digite a parte Real do segundo numero complexo: "))
                    b = float(input("Digite a parte Imaginaria do segundo numero complexo: "))
                    n2 = complexNum(a, b)

                match opc1:
                    case 1:
                        n3 = n1.soma(n2)
                        print(f"\nPrimeiro número complexo {n1.printar()}")
                        print(f"Segundo número complexo {n2.printar()}")
                        print(f"A soma dos dois numeros complexos é: {n3.printar()}")
                    case 2:
                        n3 = n1.subtracao(n2)
                        print(f"\nPrimeiro número complexo {n1.printar()}")
                        print(f"Segundo número complexo {n2.printar()}")
                        print(f"A subtração dos dois numeros complexos é: {n3.printar()}")
                    case 3:
                        n3 = n1.multiplicacao(n2)
                        print(f"\nPrimeiro número complexo {n1.printar()}")
                        print(f"Segundo número complexo {n2.printar()}")
                        print(f"A multiplicação dos dois numeros complexos é: {n3.printar()}")
                    case 4:
                        n3 = n1.divisao(n2)
                        print(f"\nPrimeiro número complexo {n1.printar()}")
                        print(f"Segundo número complexo {n2.printar()}")
                        print(f"A divisão dos dois numeros complexos é: {n3.printar()}")
                    case 5:
                        print(f"\nPrimeiro número complexo {n1.printar()}")
                        print(f"Segundo número complexo {n2.printar()}")
                        print(f"OS conjulgadoS dos dois numeros são: \n{n1.printar()} --> {(n1.conjulgado()).printar()}\n{n2.printar()} --> {(n2.conjulgado()).printar()}")
                    case 6:
                        print("\nCalculando a forma polar para o PRIMEIRO número informado:")
                        n1.forma_polar()
                    case 7: 
                        break
                    case _:
                        print("Opção inválida")
                        
        case 3: 
            print("Saindo...")
            break
        case _:
            print("Opção inválida")
