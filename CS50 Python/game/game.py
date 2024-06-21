import random

while True:
    try:
        x = int(input("Level: "))
        if x > 0:
             break
    except:
         pass

z = random.randint(1,x)

while True:
        try:
             y = int(input("Guess: "))
             if y > 0:
                if y > z:
                    print("Too large!")
                elif y < z:
                    print("Too small!")
                else:
                    print("just right!")
                    break

        except:
             pass