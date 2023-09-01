import datetime

def form_create_product():
        id_product = int(input("Id do produto: "))
        name = input("nome do produto: ")
        stock_initial = int(input("estoque inicial: "))
        stock_input = None
        print(input)
        output = None
        print(output)
        stock_actually = None
        stock_min = int(input("Estoque minimo: "))
        category = input("Categoria: ")
        date = datetime.date.today()
        log_type = "Output"
        result = [id_product, name, stock_initial, stock_input, output, stock_actually, stock_min, category, date]
        result_log = [id_product, name, stock_initial, stock_input, output, stock_actually, stock_min, category, date, log_type]
        print(result)
        return result, result_log

def form_output_product():
        data = datetime.date.today()
        id_control = int(input("ID do controle: "))
        type_E = 'S'
        cliente = input("Quem pegou o item: ")
        carro = input("Modelo do Carro: ")
        modelo = input("Placa do veículo: ")
        quantidade = input("Quantidade: ")
        id_item = int(input("ID do produto: "))
        result = [data, id_control, type_E, cliente, carro,
                   modelo, quantidade, id_item]
        type_log = "Output"
        result_log = [data, id_control, type_E, cliente, carro,
                   modelo, quantidade, id_item, data]
        return result, result_log
        

def form_input_product():
        data = datetime.date.today()
        id_control = int(input("ID do Controle: "))
        type_E = 'E'
        cliente = "ENTRADA"
        carro = "ENTRADA"
        modelo = "ENTRADA"
        quantidade = input("Quantidade: ")
        id_item = int(input("ID do produto: "))
        type_log = "input"
        result = [data, id_control, type_E, cliente, carro,
                   modelo, quantidade, id_item]
        result_log = [data, id_control, type_E, cliente, carro,
                   modelo, quantidade, id_item, None, type_log]
        return result, result_log
        
