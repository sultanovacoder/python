#коммент
print("Доброе утро")
print("privet")
name = input("Ваше имя: ")
print(name, ", добро пожаловать в мир пайтон")
answer = input("Давайте поработаем?(Y/N)")
action = "1 помыть полы"
action2 = "2 помыть посуду"
action3 = "3 подготовиться к работе"
action4 = "4 заняться выбором дизайна дома"

if answer == 'Y':
    print(action, action2, action3, action4)
    answer2 = input( "Какой действие ты хочешь сделать?(1/2/3/4)")
    print("Молодец. Ты выбрала действие: ")
    if answer2 == '1':
        print(action)
    elif answer2 == '2': 
        print(action2)
    elif answer2 == '3':
        print(action3)
    elif answer2 == '4':
        print(action4)
elif answer == 'N':
    print("До свидания!")
else:
    print("Неизвестный выбор!")