import itertools
import math
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *


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


def main():
    # window
    window = tk.Tk()
    window.title("Hour Calculator")
    window.geometry("400x300+10+10")
    window.resizable(False, False)
    window.eval('tk::PlaceWindow . center')

    # grid
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)

    # buttons
    calculate_time_button = Button(window, text="Calculate Time", bg='gray', fg='white', bd=0, padx=5, pady=2.5, command=calculate_time)
    calculate_time_button.grid(column=0, row=0, padx=5, pady=20)

    total_time_button = Button(window, text="Total Time", bg='gray', fg='white', bd=0, padx=5, pady=2.5, command=calculate_time)
    total_time_button.grid(column=1, row=0, padx=5, pady=20)

    window.mainloop()


def calculate_time():
    print("hallo")


if __name__ == '__main__':
    main()
    # while True:
    #     print("1:Add Time\n2:MultTime\n3:Multiply Time")
    #     options(int(input("Option: ")))
