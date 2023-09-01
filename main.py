from estoque import menu_stock
from control_os.spreadsheets import create_spreadsheet, data_car, data_os
from control_os.frases import action_input


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
                menu_stock()
                action = int(input(action_input))
            case 5:
                print("fim do programa")             


menu()