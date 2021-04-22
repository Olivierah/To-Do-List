def menu():
    print('=' * 30)
    print('Menu'.center(30))
    print('=' * 30)
    print('[1] - Ver lista de afazeres')
    print('[2] - Inserir novo item na lista')
    print('[3] - Remover um item da lista')
    print('[4] - Sair')

def ver_Lista():
    if len(to_Do_list) == 0:
        print('Você ainda não tem tarefas :(')
    else:
        for i in range(len(to_Do_list)):
            print(f'item [{i + 1}] - {to_Do_list[i]}')

def insere_Lista(txt):
    to_Do_list.append(txt)
    print('Nova tarefa inserida! :D')

def remove_Lista():
    if len(to_Do_list) == 0:
        print('Você ainda não tem tarefas :(')
    else:
        print('Qual tarefa vamos remover? Digite o número do item que será removido.')
        ver_Lista()
        try:
            opc = int(input('=> '))
            while opc < 0 or opc > len(to_Do_list):
                print('Opção inválida! Digite uma opção válida')
                ver_Lista()
                opc = int(input('=> '))
        except:
            print('opção inválida. Tente novamente')
        else:
            opc -= 1
            del (to_Do_list[opc])
            print('Tarefa removida com sucesso!')


to_Do_list = []

while True:
    menu()
    try:
        opc = int(input('=> '))
        while opc < 1 or opc > 4:
            print('Opção inválida! Digite uma opção entre 1 e 4')
            menu()
            opc = int(input('=> '))
    except:
        print('Opção inválida! Digite uma opção entre 1 e 4')
    else:
        if opc == 1:
            ver_Lista()
        elif opc == 2:
            print('Vamos adicionar uma nova tarefa! =D')
            txt = str(input('Qual será sua nova tarefa? '))
            insere_Lista(txt)
        elif opc == 3:
            remove_Lista()
            while len(to_Do_list) != 0:
                op = str(input('Ainda deseja remover alguma tarefa? [S/N]: ')).upper()
                if op == 'S':
                    remove_Lista()
                else:
                    break
        elif opc == 4:
            break