"""
Define funções utilitárias para realizar calculos e controle de erro
"""


def linha_erro():
    print()
    print('*********** ERRO ***********')
    print()


def erro(msg='Aconteceu um Erro'):
    mensagem = msg

    linha_erro()
    print(mensagem)
    linha_erro()


def igual_float(a):
    try:
        num1 = float(a)
        return num1
    except ValueError:
        erro('O valor da entrada precisa ser um número')
        num1 = 'erro'
        return num1


def input_numeros():
    while True:
        num1 = input('Primeiro número: ')
        num1 = igual_float(num1)

        if num1 == 'erro':
            continue
        break

    while True:
        num2 = input('Segundo número: ')
        num2 = igual_float(num2)

        if num2 == 'erro':
            continue
        break
    return num1, num2


def soma():
    print()
    print('Você escolheu ***Somar***')
    print('Entre dois números para serem somados: ')
    print()

    num1, num2 = input_numeros()

    total = num1 + num2
    print()
    print(f'O resultado da soma é {total}')
    print()


def subtracao():
    print()
    print('Você escolheu ***Subtrair***')
    print('Entre dois números para serem subtraidos: ')
    print()

    num1, num2 = input_numeros()

    total = num1 - num2
    print()
    print(f'O resultado da subtração é {total}')
    print()


def multiplicacao():
    print()
    print('Você escolheu ***Multiplicação***')
    print('Entre dois números para serem multiplicados: ')
    print()

    num1, num2 = input_numeros()

    total = num1 * num2
    print()
    print(f'O resultado da multiplicação é {total}')
    print()


def divisao():
    print()
    print('Você escolheu ***Dividir***')
    print('Escolha o primeiro número para ser divido pelo segundo número escolhido: ')
    print()

    num1, num2 = input_numeros()
    while True:
        if num2 < 1:
            erro('O segundo número tem que ser maior que 0')
            num2 = input('Segundo número: ')
            num2 = igual_float(num2)

            if num2 == 'erro':
                continue
        else:
            total = round(num1 / num2, 2)
            break

    print()
    print(f'O resultado da divisão é {total}')
    print()
    return


def porcentagem():
    print()
    print('Você escolheu ***Porcentagem***')
    print('Calcule quantos % o primeiro número é do segundo: ')
    print()

    num1, num2 = input_numeros()

    total = round((num1 * 100) / num2, 2)
    print()
    print(f'O primeiro número é igual a {total}% de {num2}')
    print()
    return
