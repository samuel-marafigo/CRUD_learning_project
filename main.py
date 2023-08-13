import time

estudantes = []  # cria lista para registro de estudantes


def menu_principal_layout():  # layout do menu principal
    print('=== MENU PRINCIPAL ===')
    print('(1) Gerenciar estudantes.')
    print('(2) Gerenciar professores.')
    print('(3) Gerenciar disciplinas.')
    print('(4) Gerenciar turmas.')
    print('(5) Gerenciar matrículas.')
    print('(9) Sair.')


def menu_principal_logica():  # lógica do menu principal, buscando separar lógica e design
    while True:
        menu_principal_layout()  # layout dentro do loop para reprintar o menu se opção inválida
        opcao = escolha_do_usuario()
        if opcao == 1:
            print('Você escolheu gerenciar: Estudantes')
            time.sleep(1)
            menu_estudantes_logica()
        elif opcao == 2:
            desenvolvimento()
        elif opcao == 3:
            desenvolvimento()
        elif opcao == 4:
            desenvolvimento()
        elif opcao == 5:
            desenvolvimento()
        elif opcao == 9:
            exit()
        else:
            print('Opção inválida!')
            time.sleep(1)
            print('Retornando ao menu principal...')
            time.sleep(1)


def menu_estudantes_layout():  # layout menu de operações - estudantes
    print('=== ESTUDANTES ===')
    print('(1) Incluir.')
    print('(2) Listar.')
    print('(3) Atualizar.')
    print('(4) Excluir.')
    print('(9) Voltar ao menu principal.')


def menu_estudantes_logica():  # lógica menu de operações - estudantes
    while True:
        menu_estudantes_layout()
        opcao = escolha_do_usuario()
        if opcao == 1:
            incluir()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            desenvolvimento()
        elif opcao == 4:
            desenvolvimento()
        elif opcao == 9:
            return
        else:
            print('Opção inválida!')


def desenvolvimento():  # placeholder das funções ainda não implementadas
    print('Em desenvolvimento')
    time.sleep(1)
    print('Retornando ao menu anterior...')
    time.sleep(1)


def incluir():  # operação de inclusão
    print('Você escolheu: Incluir')
    nome_estudante = input('Informe o nome do estudante: ')
    estudantes.append(nome_estudante)


def listar():  # operação de listagem
    print('Você escolheu: Listar')
    if len(estudantes) > 0:
        print('=== LISTA ===')
        for estudante in estudantes:
            print(estudante)
        time.sleep(2)
    else:
        print('Lista vazia...')
        time.sleep(1)


def escolha_do_usuario():  # lógica do input dos menus - passível de reutilização
    try:
        return int(input('Escolha uma opção: '))
    except ValueError:  # adicionado um block de try-except para não quebrar o código caso o usuário digite um não-int.
        print('Você precisa escolher um *número*.')
        time.sleep(1)


def menu_principal(): #loop principal
    while True:
        menu_principal_logica()


menu_principal()
