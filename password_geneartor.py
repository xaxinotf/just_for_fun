import random
import time
a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = "0123456789"
d = "[]{}()*'/,_-!?"

all = a + b + c + d
lenght = int(input("Введите длину пароля: "))
password = "".join(random.sample(all,lenght))
print("Пароль генерируеться...")
time.sleep(3)
print("Ваш пароль готов:", password)
input()
