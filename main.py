import time

estudantes = []  # cria lista para registro de estudantes


def menu_principal():  # layout e lógica do menu principal
    print('=== MENU PRINCIPAL ===')
    print('(1) Gerenciar estudantes.')
    print('(2) Gerenciar professores.')
    print('(3) Gerenciar disciplinas.')
    print('(4) Gerenciar turmas.')
    print('(5) Gerenciar matrículas.')
    print('(9) Sair.')
    try:
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            print('Você escolheu gerenciar: Estudantes')
            time.sleep(1)
            menu_estudantes()
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
    except ValueError:  # adicionado um block de try-except para não quebrar o código caso o usuário não digite um int.
        print('Opção inválida! Você precisar escolher um *número*.')
        time.sleep(1)


def menu_estudantes():  # layout e lógica do menu de operações - estudantes
    while True:
        print('(1) Incluir.')
        print('(2) Listar.')
        print('(3) Atualizar.')
        print('(4) Excluir.')
        print('(9) Voltar ao menu principal.')
        try:
            opcao = int(input('Escolha uma opção: '))
            if opcao == 1:
                incluir()
            elif opcao == 2:
                listar()
            elif opcao == 3:
                desenvolvimento()
            elif opcao == 4:
                desenvolvimento()
            elif opcao == 9:
                break
            else:
                print('Opção inválida!')
        except ValueError:
            print('Opção inválida! Você precisar escolher um *número*.')
            time.sleep(1)


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
        for i in range(len(estudantes)):
            print(estudantes[i])
        time.sleep(2)
    else:
        print('Lista vazia...')
        time.sleep(1)


while True:  # loop principal
    menu_principal()
