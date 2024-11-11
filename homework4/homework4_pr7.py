def solve_equation():
    # Функция для ввода и проверки числа
    def get_number(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Ошибка: Пожалуйста, введите число.")
    
    # Ввод значений с проверками
    a = get_number("Введите значение a: ")
    while True:
        b = get_number("Введите значение b (не должно быть 0): ")
        if b != 0:
            break
        print("Ошибка: b не должно быть равно 0.")
    c = get_number("Введите значение c: ")

    # Вычисление уравнения
    x = a / b + c * a

    print(f"Результат: x = {x}")

solve_equation()
