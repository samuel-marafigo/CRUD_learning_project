import time

dicionario_estudantes = {}  # cria dicionário para registro de dados



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
            placeholder_em_desenvolvimento()
        elif opcao == 3:
            placeholder_em_desenvolvimento()
        elif opcao == 4:
            placeholder_em_desenvolvimento()
        elif opcao == 5:
            placeholder_em_desenvolvimento()
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
            incluir_dados()
        elif opcao == 2:
            listar_dados()
        elif opcao == 3:
            atualizar_dados()
        elif opcao == 4:
            excluir_dados()
        elif opcao == 9:
            return
        else:
            print('Opção inválida!')


def placeholder_em_desenvolvimento():  # placeholder das funções ainda não implementadas
    print('Em desenvolvimento')
    time.sleep(1)
    print('Retornando ao menu anterior...')
    time.sleep(1)


def incluir_dados():
    print('Você escolheu: Incluir')
    if dicionario_estudantes:  # Hard-code do número do código para evitar duplicatas.
        codigo = max(dicionario_estudantes.keys()) + 1
    else:
        codigo = 1
    print(f'O código para este estudante será: #{codigo}')
    nome = input('Informe o nome do estudante: ')
    cpf = input('Informe o CPF do estudante: ')
    estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
    dicionario_estudantes[codigo] = estudante
    print(f"Estudante adicionado com o código {codigo}.")


def listar_dados():  # operação de listagem
    print('Você escolheu: Listar')
    if len(dicionario_estudantes) > 0:
        print('=== LISTA ===')
        for dados in dicionario_estudantes:
            print(dicionario_estudantes[dados])
        time.sleep(2)
    else:
        print('Lista vazia...')
        time.sleep(1)

def atualizar_dados():
    print('Você escolheu: Atualizar')
    try:
        codigo = int(input('Informe o código do estudante a ser atualizado: '))
        if codigo in dicionario_estudantes:
            print(f"Atualizando dados para o estudante com o código: {codigo}")
            nome = input('Informe o novo nome do estudante: ')
            cpf = input('Informe o novo CPF do estudante: ')
            estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
            dicionario_estudantes[codigo] = estudante
            print(f"Estudante atualizado com sucesso!")
        else:
            print("Estudante com o código informado não encontrado.")
    except ValueError:
        print('O código deve ser um número inteiro.')

def excluir_dados():
    print('Você escolheu: Excluir')
    try:
        codigo = int(input('Informe o código do estudante a ser excluído: '))
        if codigo in dicionario_estudantes:
            del dicionario_estudantes[codigo]
            print(f"Estudante com o código {codigo} foi excluído.")
        else:
            print("Estudante com o código informado não encontrado.")
    except ValueError:
        print('O código deve ser um número inteiro.')


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
