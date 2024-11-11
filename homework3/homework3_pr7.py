def convert_to_base_9():
    # Проверка корректности ввода числа
    while True:
        try:
            decimal = int(input("Введите десятичное число: "))
            break
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")

    # Конвертация в девятеричную систему
    result = ""
    number = decimal
    if number == 0:
        result = "0"
    else:
        while number > 0:
            result = str(number % 9) + result
            number //= 9

    print(f"Число {decimal} в девятеричной системе: {result}")

convert_to_base_9()
