# O pacote 'reportlab' deverá ser instalado para rodar o código abaixo
# pip install reportlab

from reportlab.pdfgen import canvas

def pdf(to_Do_list):
    if len(to_Do_list) > 0:
        dict = {}
        for i in range(len(to_Do_list)):
            dict[f'Tarefa {i + 1}'] = to_Do_list[i]
        try:
           nome_pdf = str(input('Qual será o nome do pdf? '))
           pdf = canvas.Canvas(f'{nome_pdf}.pdf')
           x = 720
           for indice, tarefa in dict.items():
                x-= 20
                pdf.drawString(100, x, '{}:  {}'.format(indice, tarefa))
           pdf.setTitle((nome_pdf))
           pdf.setFont('Helvetica-Oblique', 26)
           pdf.drawString(220,750, 'Lista de afazeres:')
           pdf.setFont('Helvetica-Bold', 12)
           pdf.drawString(268,724, 'Minhas tarefas :D')
           pdf.save()
           print('=' * 30)
           print(f'{nome_pdf} criado com sucesso! ')
           print('=' * 30)
        except:
           print('!' * 30)
           print(f'Erro ao criar o {nome_pdf}.pdf')
           print('!' * 30)
    else:
        print('Sua lista ainda não possui tarefas :( ')
        print('Tente adicionar novas tarefas para poder salvar no formato PDF :D')

def menu():
    print('=' * 30)
    print('Menu'.center(30))
    print('=' * 30)
    print('[1] - Ver lista de afazeres')
    print('[2] - Inserir novo item na lista')
    print('[3] - Remover um item da lista')
    print('[4] - Salvar sua lista em um PDF')
    print('[5] - Sair')

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
            while opc <= 0 or opc > len(to_Do_list):
                print('Opção inválida! Digite uma opção válida!')
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
        while opc < 1 or opc > 5:
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
            pdf(to_Do_list)
        elif opc == 5:
            break