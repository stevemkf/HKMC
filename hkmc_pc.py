import tkinter as tk
from tkinter import simpledialog, messagebox

male_pay = [5100, 5240, 5380, 5520, 5660, 5800, 5950, 6100, 6250, 6400,
            6560, 6720, 6880, 7040, 7200, 7360, 7520, 7680, 7840, 8000,
            8160, 8320, 8480, 8640, 8800, 8960]

female_pay = [4700, 4820, 4940, 5060, 5180, 5300, 5400, 5510, 5620, 5730,
              5840, 5950, 6060, 6180, 6300, 6420, 6540, 6660, 6780, 6900,
              7030, 7160, 7290, 7420, 7550, 7680]


def when_exhaust(capital: float, interest_rate: float, monthly_pay: float):
    money_left = capital
    months = 0
    while money_left >= monthly_pay:
        money_left = (money_left - monthly_pay) * (1 + interest_rate/(12*100))
        months += 1
    years, remaining_months = divmod(months, 12)
    return years, remaining_months, int(money_left)


def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    while True:
        current_age = simpledialog.askinteger("Input", "幾多歲買 (60 to 85):")
        if current_age is not None and 60 <= current_age <= 85:
            break

    while True:
        expected_age = simpledialog.askinteger("Input", "諗住有幾多歲命:")
        if expected_age is not None and expected_age > current_age:
            break

    while True:
        gender = simpledialog.askstring("Input", "男定女 ('m/f')").lower()
        if gender == "m":
            monthly_pay = male_pay[current_age - 60]
            break
        elif gender == "f":
            monthly_pay = female_pay[current_age - 60]
            break

    return current_age, expected_age, monthly_pay


current_age, expected_age, monthly_pay = get_user_input()
expected_years = expected_age - current_age
capital = 1000000.0
interest_rate = 0.00

# Loop to find the interest rate that ensures the capital lasts for the expected years
while True:
    years, remaining_months, money_left = when_exhaust(capital, interest_rate, monthly_pay)
    if years >= expected_years:
        break
    else:
        interest_rate += 0.01


messagebox.showinfo("Results", f"買一百萬, 每月派 = ${monthly_pay}\n"
                              f"{years} 年, {remaining_months} 月之後冇得派, 剩低嘅零頭係 ${money_left}\n"
                              f"等於年息: {interest_rate:.2f}%\n")

if years > expected_years:
          messagebox.showinfo("Note", "到死都未派完, 剩低嘅會派畀家人.")

