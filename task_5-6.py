print("Задание 5")
string = input("Введите 2 слова: ")
new_list = string.split()
new_list.reverse()
changed_order = " ".join(new_list)
print(changed_order)

print("Задание 6")
name = input("Введите ФИО: ")
new_list = name.split()
print(f"{new_list[0]} {new_list[1][0]}. {new_list[2][0]}.")
