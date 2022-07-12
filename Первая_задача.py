import datetime

def check_to_date(day, month, year):
    user_input = list(map(int, input("Введите дату: ").replace('.', ' ').split()))
    for _ in user_input:
        day = user_input[0]
        month = user_input[1]
        year = user_input[2]

    try:
        datetime.date(day=day, month=month, year=year)
        return "Correct date"
    except ValueError:
        return "Incorrect date"

print(check_to_date(5, 12, 2020))
