def calculate_salary():
    salary = 1_000_000
    spending_money = int(input('Сколько Вы тратите в среднем за месяц? '))
    if salary > spending_money:
        acumm = f'Будучи junior-разработчиком в нашей компании Вы сможете откладывать приблизтельно ---> {salary - spending_money} рублей'
        print(acumm)
    else:
        pass
        print('В этом месяце Вы ничего не накопили, Вам явно пора становиться middle-senior разработчиком :( ')




