import datetime
def week_day():
    print("Введите ваш день рождения: ДД")
    d = input()
    print("Введите ваш месяц рождения: ММ")
    m = input()
    print("Введите ваш год рождения: ГГГГ")
    y = input()
    date = d + " " + m + " " + y
    given_date = datetime.datetime.strptime(date, '%d %m %Y')
    day_of_week = (given_date.weekday() + 1)
    print("Ваша дата:", y + "-" + m + "-" + d, "соответствует дню недели:")
    if (day_of_week == 1):
        print("Понедельник\n")
    elif (day_of_week == 2):
        print("Вторник\n")
    elif (day_of_week == 3):
        print("Среда\n")
    elif (day_of_week == 4):
        print("Четверг\n")
    elif (day_of_week == 5):
        print("Пятница\n")
    elif (day_of_week == 6):
        print("Суббота\n")
    elif (day_of_week == 7):
        print("Воскресенье\n") 

week_day()
