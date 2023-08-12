import time
def menu_principal():
    print('=== MENU PRINCIPAL ===')
    print('(1) Gerenciar estudantes.')
    print('(2) Gerenciar professores.')
    print('(3) Gerenciar disciplinas.')
    print('(4) Gerenciar turmas.')
    print('(5) Gerenciar matrículas.')
    print('(9) Sair.')

def estudantes():
    while True:
        print('(1) Incluir.')
        print('(2) Listar.')
        print('(3) Atualizar.')
        print('(4) Excluir.')
        print('(9) Voltar ao menu principal.')
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            incluir()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            excluir()
        elif opcao == 9:
            break
        else:
            print('Opção inválida!')

def professores():
    while True:
        print('(1) Incluir.')
        print('(2) Listar.')
        print('(3) Atualizar.')
        print('(4) Excluir.')
        print('(9) Voltar ao menu principal.')
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            incluir()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            excluir()
        elif opcao == 9:
            break
        else:
            print('Opção inválida!')

def matriculas():
    while True:
        print('(1) Incluir.')
        print('(2) Listar.')
        print('(3) Atualizar.')
        print('(4) Excluir.')
        print('(9) Voltar ao menu principal.')
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            incluir()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            excluir()
        elif opcao == 9:
            break
        else:
            print('Opção inválida!')


def disciplinas():
    while True:
        print('(1) Incluir.')
        print('(2) Listar.')
        print('(3) Atualizar.')
        print('(4) Excluir.')
        print('(9) Voltar ao menu principal.')
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            incluir()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            excluir()
        elif opcao == 9:
            break
        else:
            print('Opção inválida!')


def turmas():
    while True:
        print('(1) Incluir.')
        print('(2) Listar.')
        print('(3) Atualizar.')
        print('(4) Excluir.')
        print('(9) Voltar ao menu principal.')
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            incluir()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            excluir()
        elif opcao == 9:
            break
        else:
            print('Opção inválida!')

def incluir():
    print('Você escolheu: Incluir')
    exit()

def listar():
    print('Você escolheu: Listar')
    exit()

def atualizar():
    print('Você escolheu: Atualizar')
    exit()

def excluir():
    print('Você escolheu: Excluir')
    exit()

while True:
    menu_principal()
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        print('Você escolheu gerenciar: Estudantes')
        time.sleep(1)
        estudantes()
    elif opcao == 2:
        print('Você escolheu gerenciar: Professores')
        time.sleep(1)
        professores()
    elif opcao == 3:
        print('Você escolheu gerenciar: Disciplinas')
        time.sleep(1)
        disciplinas()
    elif opcao == 4:
        print('Você escolheu gerenciar: Turmas')
        time.sleep(1)
        turmas()
    elif opcao == 5:
        print('Você escolheu gerenciar: Matrículas')
        time.sleep(1)
        matriculas()
    elif opcao == 9:
        exit()
    else:
        print('Opção inválida!')
        time.sleep(1)
        print('Retornando ao menu principal...')
        time.sleep(1)










