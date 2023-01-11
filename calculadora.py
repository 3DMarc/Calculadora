import utils as ut

# # Loop principal
while True:
    opcao = ut.menu()

    if opcao == 'q':
        print()
        print('Até a próxima...')
        quit()
    elif opcao == '1':
        ut.soma()
        loop = ut.nova_op()
    elif opcao == '2':
        ut.subtracao()
        loop = ut.nova_op()
    elif opcao == '3':
        ut.multiplicacao()
        loop = ut.nova_op()
    elif opcao == '4':
        ut.divisao()
        loop = ut.nova_op()
    elif opcao == '5':
        ut.porcentagem()
        loop = ut.nova_op()
    else:
        ut.erro('Entre um valor válido da próxima vez...')
        print()
        continue
