from spreadsheets import create_spreadsheet, data_car, data_os
from estoque import cadastrarProduto, add_entrada, add_saida
from frases import action_input


def menu():
    def criar_planilhas():
        create_spreadsheet()

    def add_veiculo():
        data_car()

    def add_os():
        data_os()

    action = int(input(action_input))
    while action != 5:
        match action:
            case 1:
                print("Vamos Criar uma planilha")
                criar_planilhas()
                action = int(input(action_input))
            case 2:
                action_car = input("voce já criou a planilha: S ou N\n").upper()
                match action_car:
                    case 'S':
                        print("Vamos Add um veiculo a planilha existente")
                        add_veiculo()
                        action = int(input(action_input))
                    case 'N':
                        print("você deve criar a planilha não se preocupe faremos isso aqui")
                        create_spreadsheet()
                        action_car = input("voce já criou a planilha: S ou N\n").upper()
            case 3:
                action_os = input("voce já criou a planilha: S ou N ").upper()
                match action_os:
                    case 'S':
                        print("Vamos Add um veiculo a planilha existente")
                        add_os()
                        action = int(input(action_input))
                    case 'N':
                        print("você deve criar a planilha não se preocupe faremos isso aqui")
                        create_spreadsheet()
                        action_os = input("voce já criou a planilha: S ou N\n").upper()
            case 4:
                action_estoque = int(input('escolha a opção\n1-Criar Produto\n2-Saida\n3-entrada\n4-Sair\n'))
                while action_estoque != 4:
                    match action_estoque:
                        case 1: 
                            cadastrarProduto()
                            print("Produto Cadastrado")
                            action_estoque = int(input('escolha a opção\n1-Criar Produto\n2-Saida\n3-entrada\n4-Sair\n'))
                        case 2:
                            add_saida()
                            print("Estoque Atualizado")
                            action_estoque = int(input('escolha a opção\n1-Criar Produto\n2-Saida\n3-entrada\n4-Sair\n'))
                        case 3: 
                            add_entrada()
                            print("Estoque Atualizado")
                            action_estoque = int(input('escolha a opção\n1-Criar Produto\n2-Saida\n3-entrada\n4-Sair\n'))
                        case 4:
                            print("Voltando ao menu inicial")
            

            case 5:
                print("fim do programa")                

menu()