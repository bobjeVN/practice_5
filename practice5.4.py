import random
print("Игра---Угадай Столицу(Европа)")
print("Если хочешь остановиться, вместо ответа напиши Stop")
print("")
city = dict(
 Austria = 'Vienna',
 Belarus = 'Minsk',
 Belgium = 'Brussels',
 Bulgaria = 'Sofia',
 Vatican = 'Vatican',
 Hungary = 'Budapest',
 Great_Britain = 'London',
 Germany = 'Berlin',
 Russia = 'Moscow',
 Ukraine = 'Kiev',
 Finland = 'Helsinki',
 France = 'Paris',
 Montenegro = 'Podgorica',
 Czech_Republic = 'Prague',
 Croatia = 'Zagreb',
 Switzerland = 'Bern',
 Sweden = 'Stockholm',
 Estonia = 'Tallinn')
counter = 0
praviln = 0
restart = True
while restart:
    country, capital = random.choice(list(city.items()))
    print(country)
    answer = str(input("Введи Ответ "))
    if answer == capital:
        print("Молодец!")
        praviln+=1
    elif answer == 'Stop':
        restart = False
        break
    else:
        print("Попробуй ещё!")
        counter+=1
    print("Правильные","Неправильные")
    print("    ",praviln,"        ",counter)
    print("                         ")