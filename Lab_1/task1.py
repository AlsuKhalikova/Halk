numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missed = 4

count = len(numbers)
total = sum(numbers[:missed]) + sum(numbers[missed+1:])

numbers[missed] = total / count
print("Измененный список:", numbers)
