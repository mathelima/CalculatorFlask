from calculator import *


def menu():
    print('Menu: \n'
          '1: Soma \n'
          '2: Subtração \n'
          '3: Multiplicação \n'
          '4: Divisão \n'
          '0: Sair')
    operacao = int(input('Digite o número da operação que deseja realizar: '))
    return operacao


while True:
    operacao = menu()
    if operacao == 0:
        exit(0)
    else:
        try:
            numero1 = float(input('Digite o primeiro número: '))
            numero2 = float(input('Digite o segundo número: '))
        except ValueError:
            print('Valor inválido!')
            exit(1)
        if operacao == 1:
            resultado = soma(numero1, numero2)
        elif operacao == 2:
            resultado = subtracao(numero1, numero2)
        elif operacao == 3:
            resultado = multiplicacao(numero1, numero2)
        elif operacao == 4:
            resultado = divisao(numero1, numero2)
        else:
            print('Operação inválida, tente novamente!')
        print(f'{resultado:.2f}')
