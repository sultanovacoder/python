#!/usr/bin/python
# coding=UTF-8
#классы ООП
import datetime
from Dog import Dog
from Client import Client
from Car import Car

my_dog = Dog('tOpik', 4)
my_dog2 = Dog('Nika',7)

print("_______команды_________")   

my_dog.sit()
my_dog2.jamp()

print("_______данные о собаках_________") 
my_dog.howyear()
my_dog2.howyear()
print()

name = 'Alina'        
print("Доброе утро, %s" % name)
print("не ленись!")
print("двумя кнопками мыши нажать на файл \"file.py\"!")
print(name, ", добро пожаловать в мир пайтон")
    
print("\nРегистрация клиента")




client1 = Client('sultanova','karina','vasilevna',1993,3,14)
client2 = Client('prokopova','lenok','artemovna',1965,7,15)
client1.setName('Evgenia')
client1.setSoname('Karpova')

client1.getFioShort()
print(client1.getYears())
client1.kormitDog(my_dog)

my_car = Car('audi','a8',2019)
#my_car.od_reading=30
print(my_car.descriptionName())
my_car.update_odometr(40)
my_car.update_odometr(20)
my_car.read_probeg()

answer = input("\n Давайте поработаем?(Y/N)")
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
