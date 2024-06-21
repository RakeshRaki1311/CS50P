def main():
    time = input("time: ")
    c_time = convert(time)
    if c_time >= 7 and c_time < 8:
        print("breakfast time")
    elif c_time >= 12 and c_time <= 13:
        print("lunch time")
    elif c_time >= 18 and c_time < 19:
        print("dinner time")


def convert(time):
    if "a.m." in time or "p.m." in time:
        hours_minutes, pm_am = time.split(" ")
        hours, minutes = hours_minutes.split(":")
        if pm_am == "p.m." and int(hours)!= 12:
            hours = int(hours) + 12
    else:
        hours,minutes = time.split(":")
    hours = float(hours) + (float(minutes) / 60)
    return hours

if __name__ == "__main__":
    main()