import openpyxl
from openpyxl.styles import PatternFill #Подключаем стили для ячеек
import os

all_files = os.listdir() # Читаем все файлы в директории в список
xls_files = [] # Объявляем список куда сложим все файлы xlsx

# Из всего списка файлов формируем список файло xls
# НАЧАЛО
for i in range(0,len(all_files)):
    if all_files[i].endswith('xlsx'):
        xls_files.append(all_files[i])
        print (i," ", all_files[i])
# КОНЕЦ

for tmp_file in xls_files:
    wb = openpyxl.load_workbook(filename = tmp_file)
    for i in wb.sheetnames:
        ws=wb[i]

        print("Лист - ", i)
        end_row = ws.max_row + 1
        end_column = ws.max_column + 1

        for i in range(1,end_row):
            for j in range(1, end_column):
                temp_value = str(ws.cell(row=i, column=j).value)

                if temp_value == "do":
                    ws.cell(row=i, column=end_column).value = "Нашел !!!"

                print(temp_value, end=" ")
                ws.cell(row=i, column=j).value = temp_value

                # ws.cell(row=i, column=j).fill = PatternFill(fill_type='solid', start_color='ff0000', end_color='ff0000')
                # Проверить и подсветить в искодном файле

            print() # Перевод строки


    #if os.path.exists('Мазгаз_1.xlsx'): os.remove('Мазгаз_1.xlsx')
    #wb.save('Мазгаз_1.xlsx')

