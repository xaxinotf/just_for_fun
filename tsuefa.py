import random

choices = ["Камень", "Ножницы", "Бумага"]

def get_player_choice():
    while True:
        player_choice = input("Выберите: Камень, Ножницы или Бумага: ")
        if player_choice in choices:
            return player_choice
        else:
            print("Некорректный ввод. Пожалуйста, выберите Камень, Ножницы или Бумага.")

player_choice = get_player_choice()
computer_choice = random.choice(choices)

print(f"Ваш выбор: {player_choice}")
print(f"Выбор компьютера: {computer_choice}")

if player_choice == computer_choice:
    print("Ничья!")
elif (player_choice == "Камень" and computer_choice == "Ножницы") or \
     (player_choice == "Ножницы" and computer_choice == "Бумага") or \
     (player_choice == "Бумага" and computer_choice == "Камень"):
    print("Ура, ты победил!")
else:
    print("Увы, ты проиграл :(")