from spreadsheets import create_spreadsheet, data_car, data_os
from estoque.menu_stock import menu_stock
from frases import action_input
import sys
import os

# Obtém o diretório do módulo menu_stock.py
module_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "estoque")

# Adiciona o diretório ao caminho de pesquisa
sys.path.append(module_directory)
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
                stock = menu_stock()
            

            case 5:
                print("fim do programa")                

menu()