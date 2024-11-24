def calculator():
    print("Простой калькулятор")
    print("Выберите операцию: +, -, *, /")
    operation = input("Введите операцию: ")

    if operation in ['+', '-', '*', '/']:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Ошибка: деление на ноль"

        return f"Результат: {result}"
    else:
        return "Неверная операция"


print(calculator())