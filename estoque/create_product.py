from openpyxl import load_workbook
from form_stock import form_create_product
import os

def create_product():
    try:
        current_directory = os.getcwd()
        print(current_directory)
        xlsx_file_path = r'C:\Users\viery\OneDrive\Documentos\GitHub\SpreadMailPro\estoque/estoque.xlsx'
        workbook = load_workbook(filename=xlsx_file_path)
        page_control = workbook['logs_new_product']
        logs_consult = workbook['logs']
        result, result_log = form_create_product()
        print(result, result_log)
        page_control.append(result)
        logs_consult.append(result_log)
        workbook.save(filename=xlsx_file_path)
        print("Produto Cadastrado com Sucesso")
    except Exception as e:
        print("Algo deu errado")
        print(e)


create_product()