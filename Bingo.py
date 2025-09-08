import random
columnas =5
filas = 5

num = random.sample(range(1,51),25)
talon = [[random.choice(num)for _ in range(5)]for _ in range(5)]
for filas in talon:
    for elementos in talon:
        if elementos == elementos:
            random.choice(num)
print(talon)

