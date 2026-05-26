import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

n = random.randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
    except ValueError:
        continue
    if guess < n:
        print("Too small!")
    elif guess > n:
        print("Too large!")
    else:
        print("Just right!")
        break
