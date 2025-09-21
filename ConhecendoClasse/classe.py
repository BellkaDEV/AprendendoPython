import math
import os

class Retangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def area(self):
    return self.base * self.altura


class Esfera:
  def __init__(self, raio):
    self.raio = raio

  def volume(self):
    return (4/3) * math.pi * (self.raio ** 3)


def menu():
  print("__--_Menu_--__")
  print("1. Retangulo")
  print("2. Esféra")
  print("3. Sair")


op = 0
1
1
while op != 3:
  menu()
  try:
    op = int(input("Opção: "))
    if (op == 1):
      base = float(input("Informe a base: "))
      altura = float(input("Informe a altura: "))
      ret = Retangulo(base, altura)
      print(f"A area do retangulo é: {ret.area()}")
    elif (op == 2):
      raio = float(input("Informe o raio: "))
      esf = Esfera(raio)
      print(f"O volume da esféra é: {esf.volume()}")
    elif op == 3:
      print("Encerrando...")
    else:
      print("Opção inválida. Tente novamente.")
  except (ValueError, IndexError):
    print("Entrada inválida. Certifique-se de fornecer números e no formato correto.")
    
    
  if op != 3:
    input("\nPressione Enter para continuar...")
    os.system('cls')

  