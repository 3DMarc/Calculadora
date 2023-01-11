"""
Define funções utilitárias para realizar calculos e controle de erro
"""
resultado_total = 0
utilizar_total = False


def linha_erro():
    print()
    print('*********** ERRO ***********')
    print()


def erro(msg='Aconteceu um Error'):
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


def input_numeros(msg='Escolha um número: '):
    input_msg = msg
    while True:
        num = input(input_msg)
        num = igual_float(num)

        if num == 'erro':
            continue
        break
    return num


def soma():
    print()
    print('Você escolheu ***Somar***')
    print('Entre dois números para serem somados: ')
    print()
    global resultado_total
    global utilizar_total
    if utilizar_total == False:
        num1 = input_numeros('Primeiro número: ')
    else:
        num1 = resultado_total
        print(f'Primeiro número é {num1}')
    num2 = input_numeros('Segundo número: ')

    total = num1 + num2
    resultado_total = total
    print()
    print(f'O resultado da soma é {total}')
    print()
    return total


def subtracao():
    print()
    print('Você escolheu ***Subtrair***')
    print('Entre dois números para serem subtraidos: ')
    print()
    global resultado_total
    global utilizar_total
    if utilizar_total == False:
        num1 = input_numeros('Primeiro número: ')
    else:
        num1 = resultado_total
        print(f'Primeiro número é {num1}')
    num2 = input_numeros('Segundo número: ')

    total = num1 - num2
    resultado_total = total
    print()
    print(f'O resultado da subtração é {total}')
    print()
    return total


def multiplicacao():
    print()
    print('Você escolheu ***Multiplicação***')
    print('Entre dois números para serem multiplicados: ')
    print()

    global resultado_total
    global utilizar_total
    if utilizar_total == False:
        num1 = input_numeros('Primeiro número: ')
    else:
        num1 = resultado_total
        print(f'Primeiro número é {num1}')
    num2 = input_numeros('Segundo número: ')

    total = num1 * num2
    resultado_total = total
    print()
    print(f'O resultado da multiplicação é {total}')
    print()
    return total


def divisao():
    print()
    print('Você escolheu ***Dividir***')
    print('Escolha o primeiro número para ser divido pelo segundo número escolhido: ')
    print()

    global resultado_total
    global utilizar_total
    if utilizar_total == False:
        num1 = input_numeros('Primeiro número: ')
    else:
        num1 = resultado_total
        print(f'Primeiro número é {num1}')
    num2 = input_numeros('Segundo número: ')
    while True:
        if num2 < 1:
            erro('O segundo número tem que ser maior que 0')
            num2 = input('Segundo número: ')
            num2 = igual_float(num2)

            if num2 == 'erro':
                continue
        else:
            total = round(num1 / num2, 2)
            resultado_total = total
            break

    print()
    print(f'O resultado da divisão é {total}')
    print()
    return total


def porcentagem():
    print()
    print('Você escolheu ***Porcentagem***')
    print('Calcule quantos % o primeiro número é do segundo: ')
    print()
    global utilizar_total
    num1 = input_numeros('Primeiro número: ')
    num2 = input_numeros('Segundo número: ')

    total = round((num1 * 100) / num2, 2)
    utilizar_total = False
    print()
    print(f'O primeiro número é igual a {total}% de {num2}')
    print()
    return total


def menu():
    # Menu
    print('*****************************************')
    print('Selecione a operação que deseja realizar')
    print('*****************************************', '\n')
    print('-------------------')
    print('(1) Soma')
    print('(2) Subtração')
    print('(3) Multiplicação')
    print('(4) Divisão')
    print('(5) Porcentagem')
    print('(Q) Sair')
    print('-------------------', '\n')
    print('Para selecionar, por favor digite o número ou letra correspondente')
    opcao = input().lower()
    return opcao


def nova_op():
    # Checar se quer repetir a operação
    while True:
        print('Você deseja realizar uma nova operação? (S) Sim ou (N) Não?')
        resposta = input().lower()
        print()
        global utilizar_total
        if resposta == 's' and utilizar_total == True:
            while True:
                print('Você deseja utilizar o Total anterior? (S) Sim ou (N) Não?')
                resposta2 = input().lower()
                if resposta2 == 's':
                    utilizar_total = True
                    break
                elif resposta2 == 'n':
                    utilizar_total = False
                    break
                else:
                    erro('Entre um valor válido da próxima vez...')
            break
        elif resposta == 's':
            break
        elif resposta == 'n':
            print()
            print('Até a próxima...')
            quit()
        else:
            erro('Entre um valor válido da próxima vez...')
            continue
    return
