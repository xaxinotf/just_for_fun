import random

def guess_the_number():
    print("Добро пожаловать в игру 'Угадай число!'")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Введите число от 1 до 100: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Загаданное число больше")
            elif user_guess > number_to_guess:
                print("Загаданное число меньше")
            else:
                print(f"Ура! Ты угадал число {number_to_guess} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")

guess_the_number()