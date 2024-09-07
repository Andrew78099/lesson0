def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result = result + i
        except TypeError as t_e:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return [result, incorrect_data]

def calculate_average(numbers):
    try:
        aver = personal_sum(numbers)
        average = aver[0] / len(numbers)
        return average
    except ZeroDivisionError as d_z:
        return 0
    except TypeError as t_er:
        print('В numbers записан некорректный тип данных')



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать