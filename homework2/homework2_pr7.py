def convert_number():
    while True:
        try:
            decimal = int(input("Введите десятичное число: "))
            break
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")

    binary = bin(decimal)[2:]
    octal = oct(decimal)[2:]

    print(f"Двоичное представление: {binary}")
    print(f"Восьмеричное представление: {octal}")

convert_number()
