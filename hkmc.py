from flask import Flask, render_template, redirect, request

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


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("getinputs.html")


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        current_age = int(request.form['current_age'])
        expected_age = int(request.form['expected_age'])
        gender = request.form['gender'].lower()

        if gender == "m":
            monthly_pay = male_pay[current_age - 60]
        elif gender == "f":
            monthly_pay = female_pay[current_age - 60]
        else:
            return "Invalid gender input", 400

        expected_years = expected_age - current_age
        capital = 1000000.0
        interest_rate = 0.00

        while True:
            years, remaining_months, money_left = when_exhaust(capital, interest_rate, monthly_pay)
            if years >= expected_years:
                break
            else:
                interest_rate += 0.01

        return render_template("results.html", monthly_pay=monthly_pay, years=years, remaining_months=remaining_months,
                               money_left=money_left, interest_rate=round(interest_rate, 2), expected_years=expected_years)

if __name__ == '__main__':
    app.run(debug=True)