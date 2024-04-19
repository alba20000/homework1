print("Задание 14")
array = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]
]
print(array)
transposed_array = [[0 for j in range(len(array))] for i in range(len(array[0]))]
for i in range(len(array)):
    for j in range(len(array[0])):
        transposed_array[j][i] = array[i][j]
print(transposed_array)
