# Downloaded from GIT
# Коменотировать несколько строк - Выделить и нажать Ctrl + /
# Выделить несколько строк - Выделить и нажать TAB

# Список
a_list = [45, 11, 234]
a_list.append(122)
a_list.append(142)
a_list.append(16)
a_list.append(27)
# Сортируем
a_list.sort()
print(type(a_list), "  ", a_list)
# Переворачиваем
a_list.reverse()
print(type(a_list), "  ", a_list)
# Добавляем пару элементов
a_list.append("142")
a_list.append("16")
print(type(a_list), "  ", a_list)

# Словарь
a_dict = {}
a_dict[1] = 5
a_dict[2] = "5"
a_dict[6] = 3
a_dict[4] = 12
print(type(a_dict), "  ", a_dict)

# Кортеж
a_tuple = (2, 5, "678", 9, 0, -1, 45, 2, 9)  # Кортеж - неизменяемый список
print(type(a_tuple), "  ", a_tuple)

# Множества
a_set = {2, 5, 678, 9, 0, -1, 45, 2}  # Множества - можно сказать что список неповторяемых значений
print(type(a_set), "  ", a_set)
