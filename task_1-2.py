print("Задание 1")
string = input("Введите строку: ")
reversed_string = string[::-1]
print(reversed_string)

print("Задание 2")
string = input("Введите строку с буквами h: ")
first = string.find("h") + 1
string2 = string[first:]
print(string[:first] + string2.replace("h", "H", string2.count("h") - 1))
