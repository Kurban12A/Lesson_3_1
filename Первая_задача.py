def check_to_date(day, month, year):
    user_input = list(map(int, input().replace('.', ' ').split()))
    for _ in user_input:
        day = user_input[0]
        month = user_input[1]
        year = user_input[2]

        if day <= 31 and day != 0 and month <= 12 and month != 0 and len(str(year)) == 4 and year != 0:
            return 'OK'
        else:
            return 'FAILED'

print(check_to_date(28, 11, 1999))