while True:
    num = input("Fraction: ")
    index = num.find("/")
    try:
        x = int(num[:index])
        y = int(num[index+1:])
        fraction = x / y
        if x > y:
            continue
        break

    except (ValueError, ZeroDivisionError):
        continue
percentage = round(fraction * 100)
if fraction > 0.9:
    print("F")
elif fraction < 0.1:
    print("E")
else:
    print(f"{int(percentage)}%")