print("Задание 10")
list1 = input("Введите последовательность чисел: ").split()
print(len(list1) == len(set(list1)))

print("Задание 11")
date_dict = {"year": 2024, "month": 4, "day": 14}
print(f"{date_dict["year"]}-{date_dict["month"]}-{date_dict["day"]}")

print("Задание 12")
string = input("Введите последовательность чисел через запятую: ")
new_list = list(map(int, string.split(",")))
new_tuple = tuple(new_list)
print(new_list, new_tuple)
