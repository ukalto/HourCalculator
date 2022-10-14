import math
import os


def addCalcTime(hour, minute):
    if minute >= 60:
        minute %= 60
        hour += 1
    if hour >= 24:
        hour %= 24
    print(str(hour) + ":" + str(minute))


def multCalcTime(hour, minute, multiplier):
    minute *= multiplier
    add_hour = math.trunc(minute / 60)
    minute %= 60
    hour = ((hour * multiplier) + add_hour) % 24
    print(str(hour) + ":" + str(minute))


def multiplyCalcTime(hour, minute, multiplier):
    minute *= multiplier
    add_hour = math.trunc(minute / 60)
    minute %= 60
    hour = (hour * multiplier) + add_hour
    print(str(hour) + ":" + str(minute))


def options(option):
    os.system('cls')
    curr_hour = int(input("Hour:"))
    curr_minute = int(input("Minute:"))
    if option == 1:
        hour_to_add = int(input("Hours to add:"))
        minute_to_add = int(input("Minutes to add:"))
        addCalcTime(curr_hour + hour_to_add, curr_minute + minute_to_add)
    elif option == 2 or option == 3:
        multiplier = int(input("Multiplier:"))
        if option == 2:
            multCalcTime(curr_hour, curr_minute, multiplier)
        if option == 3:
            multiplyCalcTime(curr_hour, curr_minute, multiplier)


if __name__ == '__main__':
    while True:
        print("1:Add Time\n2:MultTime\n3:Multiply Time\n")
        options(int(input("Option: ")))
