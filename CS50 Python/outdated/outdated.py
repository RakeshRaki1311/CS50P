dict = ["January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ").strip()
    if "/" in date:
        month,day,year = date.split("/")
    elif "," in date:
        date = date.replace(",","")
        month,day,year = date.split(" ")
        if month in dict:
            month = dict.index(month) + 1
    elif " " in date:
        continue
    try :
        if int(month) > 12 or int(day) > 31:
            continue
        else:
            break
    except ValueError:
        continue

print(f"{year}-{int(month):02}-{int(day):02}")