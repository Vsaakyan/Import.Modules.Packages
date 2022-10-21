from application.salary import calculate_salary
from application.db.people import get_employess
from datetime import date


def time_now():
    now = date.today()
    today = f'TODAY IS -------> {now}'
    print(today)


if __name__ == '__main__':
    time_now()
    get_employess()
    calculate_salary()





