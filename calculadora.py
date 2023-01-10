import utils as ut


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
        print()
        print('Você deseja realizar uma nova operação? (S) Sim ou (N) Não?')
        resposta = input().lower()
        print()
        if resposta == 's':
            break
        elif resposta == 'n':
            print()
            print('Até a próxima...')
            quit()
        else:
            ut.erro('Entre um valor válido da próxima vez...')
            continue
    return


# Loop principal
while True:
    opcao = menu()

    if opcao == 'q':
        print()
        print('Até a próxima...')
        quit()
    elif opcao == '1':
        ut.soma()
        loop = nova_op()
    elif opcao == '2':
        ut.subtracao()
        loop = nova_op()
    elif opcao == '3':
        ut.multiplicacao()
        loop = nova_op()
    elif opcao == '4':
        ut.divisao()
        loop = nova_op()
    elif opcao == '5':
        ut.porcentagem()
        loop = nova_op()
    else:
        ut.erro('Entre um valor válido da próxima vez...')
        print()
        continue
