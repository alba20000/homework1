print("Задание 7")
nested_list = []
nested_list.extend([2, [3.4, [5+2j, [[], 6, "Иголка"]]]])
print(nested_list)

print("Задание 8")
list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]
list3 = list1 + list2
list1.extend(list2)
print(list3, list1)

print("Задание 9")
list1 = [4, 1, 3, 2]
list2 = [3, 5, 6, 4]
list3 = sorted(list1+list2)
print(set(list3))
