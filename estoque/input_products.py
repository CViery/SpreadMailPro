from openpyxl import load_workbook
import datetime
from form_stock import form_input_product
import os


def input_products():
    try:
        current_directory = os.getcwd()
        print(current_directory)
        xlsx_file_path = r'C:\Users\viery\OneDrive\Documentos\GitHub\SpreadMailPro\estoque/estoque.xlsx'
        workbook = load_workbook(filename=xlsx_file_path)
        logs_control= workbook['logs_controle']
        logs_input= workbook['logs_input']
        logs = workbook['logs']
        result, result_log = form_input_product()
        # Adiciona uma nova linha à nova planilha
        logs_control.append(result)
        logs_input.append(result_log)
        logs.append(result_log)
        
        workbook.save(filename=xlsx_file_path)
        print('Produto Atualizado no Estoque')

    except Exception as e:
        print(e)

input_products()