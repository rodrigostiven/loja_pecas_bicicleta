BICICLETARIA = {}

name = input('Digite seu nome: ')


def menu_consulta():
    print('######################################################')
    print('## 1 - Consultar Todas as Peças                     ##')
    print('## 2 - Consultar Peças por Código                   ##')
    print('## 3 - Consultar Peças por Fabricante               ##')
    print('## 4 - Retornar                                     ##')
    print('######################################################')

def consultar_pecas():
    while True:
        menu_consulta()

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            mostrar_pecas()
        elif opcao == '2':
            codigo = input('Digite o código da peça para consulta: ')
            buscar_pecas(codigo)
        elif opcao == '3':
            pass
        elif opcao == '4':
            imprimir_menu()
            break

def mostrar_pecas():
    if BICICLETARIA:
        for codigo in BICICLETARIA:
            buscar_pecas(codigo)
    else:
        print('>>>>> Bicicletaria Vazia')

def buscar_pecas(codigo):
    try:
        print('Código:', codigo)
        print('Nome:', BICICLETARIA[codigo]['nome'])
        print('Fabricante:', BICICLETARIA[codigo]['fabricante'])
        print('Valor:', BICICLETARIA[codigo]['valor'])
        print('######################################')
    except KeyError:
        print('>>>>> Peça Inexistente')
    except Exception as error:
        print('>>>>> Um erro inesperado ocorreu')
        print(error)

def ler_detalhes_contato():
    nome = input('Digite o nome da peça: ')
    fabricante = input('Digite o fabricante da peça: ')
    valor = input('Digite o valor da peça: ')
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

    print("Bem vindo ao Controle de Estoque da Bicicletaria do {}".format(name))
    print('######################################################')
    print('## 1 - Consultar Peça                               ##')
    print('## 2 - incluir Peça                                 ##')
    print('## 3 - Editar Peça                                  ##')
    print('## 4 - Excluir Peça                                 ##')
    print('## 0 - Fechar Bicicletaria                          ##')
    print('######################################################')

while True:

    imprimir_menu()

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
       consultar_pecas()
    elif opcao == '2':
        codigo = input('Digite o código da peça: ')

        try:
            BICICLETARIA[codigo]
            print('>>>>> Peça de código {} já existente'.format(codigo))

        except KeyError:
            nome, fabricante, valor = ler_detalhes_contato()
            incluir_editar_peca(codigo, nome, fabricante, valor)

    elif opcao == '3':
        codigo = input('Digite o código da peça: ')

        try:
            BICICLETARIA[codigo]
            print('>>>>> Editando peça de código ', codigo)

            nome, fabricante, valor = ler_detalhes_contato()
            incluir_editar_peca(codigo, nome, fabricante, valor)

        except KeyError:
            print('>>>>>> Peça inexistente')


    elif opcao == '4':
        codigo = input('Digite o código da peça: ')
        excluir_peca(codigo)

    elif opcao == '0':
        print('>>>>>Fechando Programa<<<<<')
        break
    else:
        print('>>>>>Opção Inválida<<<<<')