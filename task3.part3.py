numbers = list(map(int, input("Введите числа через пробелы: ").split()))
num = int(input("Введите любое число: "))
def shifts(list_of_numbers, pos_or_neg):
    if pos_or_neg <= 0:
        list_of_numbers.append(list_of_numbers.pop(0))
    elif pos_or_neg > 0:
        list_of_numbers.insert(0, list_of_numbers.pop())
shifts(numbers, num)
print(f'Ваш результат:\n\n{numbers}')
