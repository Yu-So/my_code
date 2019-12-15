import openpyxl
from openpyxl.styles import PatternFill #Подключаем стили для ячеек
import os

dict_list = []
with open('dictionary.txt') as f_dictionary:
     for word_line in f_dictionary: dict_list.append(word_line.split("\n")[0])
# print (dict_list.count("хerox"))

all_files = os.listdir() # Читаем все файлы в директории в список
xls_files = [] # Объявляем список куда сложим все файлы xlsx

# Из всего списка файлов формируем список файло xls
# НАЧАЛО
for i in range(0,len(all_files)):
    if all_files[i].endswith('.xlsx') and all_files[i].find("_1") == -1:
        xls_files.append(all_files[i])
# КОНЕЦ

for tmp_file in xls_files:
    wb = openpyxl.load_workbook(filename = tmp_file)
    for k in wb.sheetnames:

        ws=wb[k]

        end_row = ws.max_row + 1
        end_column = ws.max_column + 1

        for i in range(1,end_row):
            for j in range(1, end_column):
                temp_value = str(ws.cell(row=i, column=j).value)


                for dict_line_tmp in dict_list:
                    ####
                    if temp_value.lower().find(dict_line_tmp) != -1:
                        ws.cell(row=i, column=end_column).value = "Нашел !!!"
                        ws.cell(row=i, column=end_column+1).value = dict_line_tmp
                    # Записывать значение никуда не нужно, оно ведь уже содержится в ws


                print (tmp_file," ", wb[k]," ", i," ",j)

                # ws.cell(row=i, column=j).fill = PatternFill(fill_type='solid', start_color='ff0000', end_color='ff0000')
                # Проверить и подсветить в искодном файле

    just_first_part_of_file_name = tmp_file.split(".xlsx")[0]

    name_with_1_and_xls = just_first_part_of_file_name + "_1.xlsx"

    if os.path.exists(name_with_1_and_xls): os.remove(name_with_1_and_xls)
    wb.save(name_with_1_and_xls)

