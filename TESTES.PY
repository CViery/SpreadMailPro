import openpyxl

teste = openpyxl.load_workbook('estoque.xlsx')
print(teste)

for pag in teste:
    print(pag)

    FTG-0298