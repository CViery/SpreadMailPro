from openpyxl import load_workbook
import datetime
from form_stock import form_output_product
import os




def output_product():
    try:
        current_directory = os.getcwd()
        print(current_directory)
        xlsx_file_path = r'C:\Users\viery\OneDrive\Documentos\GitHub\SpreadMailPro\estoque/estoque.xlsx'
        workbook = load_workbook(filename=xlsx_file_path)
        logs_control= workbook['logs_controle']
        logs_output= workbook['logs_output']
        logs = workbook['logs']
        result, result_log = form_output_product() 
        logs_control.append(result)
        logs_output.append(result_log)
        logs.append(result_log)
        workbook.save(filename=xlsx_file_path)
        print('registrando logs de saida')
        print("-------------------")
        print("Registrando Logs Geral")
        print("-------------------")
        print("Registrando Controle")
        print("-------------------")
        print(f'Saida registrada.....\nsaida do produto:\n{result}')

    except Exception as e:
        print(e)

output_product()
