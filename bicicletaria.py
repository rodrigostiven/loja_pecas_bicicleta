BICICLETARIA = {}

def mostrar_pecas():
    if BICICLETARIA:
        for pecas in BICICLETARIA:
            buscar_pecas(pecas)
    else:
        print('>>>>> Bicicletaria Vazia')

def buscar_pecas(pecas):
    try:
        print('Nome:', pecas)
        print('Fabricante:', BICICLETARIA[pecas]['fabricante'])
        print('Valor:', BICICLETARIA[pecas]['valor'])
        print('######################################')
    except KeyError:
        print('>>>>> Peça Inexistente')
    except Exception as error:
        print('>>>>> Um erro inesperado ocorreu')
        print(error)


def ler_detalhes_contato():
    nome = input('Digite o telefone de contato: ')
    fabricante = input('Digite o email de contato: ')
    valor = input('Digite o endereço de contato: ')
    return (nome, fabricante, valor)


def incluir_editar_peca(codigo,nome,fabricante, valor):
    BICICLETARIA[codigo] = {
        'nome': nome,
        'fabricante': fabricante,
        'valor': valor
    }
    print()
    print('>>>>>>>>Peça de código {} adicionado/editado com sucesso'.format(codigo))
    print()

def excluir_peca(codigo):
    try:
        BICICLETARIA.pop(codigo)
        print()
        print('>>>>>Peça de código {} excluido com sucesso'.format(codigo))
        print()
    except KeyError:
        print('>>>>>Peça inexistente')
    except Exception as error:
        print('>>>>> Um erro inesperado ocorreu')
        print(error)

def imprimir_menu():
    print('#############################################')
    print('## 1 - Mostrar todos os contatos da agenda ##')
    print('## 2 - Buscar contato                      ##')
    print('## 3 - incluir contato                     ##')
    print('## 4 - Editar contato                      ##')
    print('## 5 - Excluir contato                     ##')
    print('## 0 - Fechar agenda                       ##')
    print('#############################################')

while True:

    imprimir_menu()

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        mostrar_pecas()
    elif opcao == '2':
        peca = input('Digite o nome do contato: ')
        buscar_pecas(peca)
    elif opcao == '3':
        codigo = input('Digite o código da peça: ')

        try:
            BICICLETARIA[codigo]
            print('>>>>> Peça de código {} já existente'.format(codigo))

        except KeyError:
            nome, fabricante, valor = ler_detalhes_contato()
            incluir_editar_peca(codigo, nome, fabricante, valor)

    elif opcao == '4':
        codigo = input('Digite o nome do contato: ')

        try:
            BICICLETARIA[codigo]
            print('>>>>> Editando peça', codigo)

            nome, fabricante, valor = ler_detalhes_contato()
            incluir_editar_peca(codigo, nome, fabricante, valor)

        except KeyError:
            print('>>>>>> Contato inexistente')


    elif opcao == '5':
        codigo = input('Digite o código da peça: ')
        excluir_peca(codigo)

    elif opcao == '0':
        print('>>>>>Fechando Programa<<<<<')
        break
    else:
        print('>>>>>Opção Inválida<<<<<')