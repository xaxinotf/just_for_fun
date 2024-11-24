import time

def countdown():
    seconds = int(input("Введите количество секунд для обратного отсчета: "))
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Время вышло!")

countdown()