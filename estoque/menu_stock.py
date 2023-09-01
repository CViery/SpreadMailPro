from create_product import create_product
from output_product import output_product
from input_products import input_products


def menu_stock():
     action_estoque = int(input('escolha a opção\n1-Criar Produto\n2-Saida\n3-entrada\n4-Sair\n'))
     while action_estoque != 4:
        match action_estoque:
            case 1: 
                create_product()
                print("Produto Cadastrado")
                action_estoque = int(input('escolha a opção\n1-Criar Produto\n2-Saida\n3-entrada\n4-Sair\n'))
            case 2:
                output_product()
                print("Estoque Atualizado")
                action_estoque = int(input('escolha a opção\n1-Criar Produto\n2-Saida\n3-entrada\n4-Sair\n'))
            case 3: 
                input_products
                print("Estoque Atualizado")
                action_estoque = int(input('escolha a opção\n1-Criar Produto\n2-Saida\n3-entrada\n4-Sair\n'))
            case 4:
                print("Voltando ao menu inicial")
        return action_estoque