def celsius_to_fahrenheit(celsius):

    return (celsius * 9/5) + 32



def fahrenheit_to_celsius(fahrenheit):

    return (fahrenheit - 32) * 5/9



def celsius_to_kelvin(celsius):

    return celsius + 273.15



def kelvin_to_celsius(kelvin):

    return kelvin - 273.15



def fahrenheit_to_kelvin(fahrenheit):

    return (fahrenheit - 32) * 5/9 + 273.15



def kelvin_to_fahrenheit(kelvin):

    return (kelvin - 273.15) * 9/5 + 32



print("Конвертер температур")

print("Выберите тип конвертации:")

print("1. Цельсий в Фаренгейт")

print("2. Фаренгейт в Цельсий")

print("3. Цельсий в Кельвин")

print("4. Кельвин в Цельсий")

print("5. Фаренгейт в Кельвин")

print("6. Кельвин в Фаренгейт")



choice = input("Введите номер конвертации (1-6): ")



if choice == '1':

    celsius = float(input("Введите температуру в Цельсиях: "))

    print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")

elif choice == '2':

    fahrenheit = float(input("Введите температуру в Фаренгейтах: "))

    print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.2f}°C")

elif choice == '3':

    celsius = float(input("Введите температуру в Цельсиях: "))

    print(f"{celsius}°C = {celsius_to_kelvin(celsius):.2f}K")

elif choice == '4':

    kelvin = float(input("Введите температуру в Кельвинах: "))

    print(f"{kelvin}K = {kelvin_to_celsius(kelvin):.2f}°C")

elif choice == '5':

    fahrenheit = float(input("Введите температуру в Фаренгейтах: "))

    print(f"{fahrenheit}°F = {fahrenheit_to_kelvin(fahrenheit):.2f}K")

elif choice == '6':

    kelvin = float(input("Введите температуру в Кельвинах: "))

    print(f"{kelvin}K = {kelvin_to_fahrenheit(kelvin):.2f}°F")

else:

    print("Неправильный выбор. Пожалуйста, выберите номер от 1 до 6.")