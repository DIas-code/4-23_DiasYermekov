# Ввод строки значений через input
data = input("Введите строку значений, разделённых пробелами:\n").split()

# Деление на три потока
first = data[0::3]
second = data[1::3]
third = data[2::3]

# Правила отступов и "след страница"
spacing_rules = {
    14: 1,
    15: 3,
    16: 2,
    17: "след страница",
    18: 2,
    21: 2,
    22: 3,
    23: 4,
    24: 2,
    25: 3,
    26: 4,
    27: 2,
    28: 5,
    29: 1,
    30: 3,
    31: 1,
    32: "след страница",
    33: 1,
    34: 1,
    37: 2,
    38: 3,
    40: 1,
    41: 3,
    42: 2,
    43: 3,
    44: 2,
    45: 2,
    46: 2,
    47: 2,
    48: 2,
    50: 1,
    52: 1,
    53: "след страница",
}

# Универсальная функция для вывода потока в указанный файловый объект (по умолчанию sys.stdout)
def print_stream(stream, label, out_file, interpret_third=False, replace_dots=False):
    # Записываем заголовок
    print(f"\n{label}", file=out_file)
    for idx, item in enumerate(stream, 1):  # Нумерация начинается с 1
        output = item

        # Если для второго потока замена точек на запятые
        if replace_dots:
            output = output.replace('.', ',')

        # Если требуется интерпретация для третьего потока (оценки)
        if interpret_third:
            if item == '5':
                output = item + ' (отлично)'
            elif item == '4':
                output = item + ' (хорошо)'
            elif item == '3':
                output = item + ' (удов.)'

        print(output, file=out_file)

        # Проверка и применение правил отступов/вставок
        if idx in spacing_rules:
            rule = spacing_rules[idx]
            if isinstance(rule, int):
                print("\n" * rule, end='', file=out_file)
            elif isinstance(rule, str):
                print(rule, file=out_file)
                print(file=out_file)

# Запись вывода каждого потока в отдельный текстовый файл
with open('first_output.txt', 'w', encoding='utf-8') as f_first, \
     open('second_output.txt', 'w', encoding='utf-8') as f_second, \
     open('third_output.txt', 'w', encoding='utf-8') as f_third:
     
    print_stream(first, "Первый поток (1, 4, 7...)", f_first)
    print_stream(second, "Второй поток (2, 5, 8...)", f_second, replace_dots=True)
    print_stream(third, "Третий поток (3, 6, 9...)", f_third, interpret_third=True)

print("Вывод записан в файлы: first_output.txt, second_output.txt, third_output.txt")

