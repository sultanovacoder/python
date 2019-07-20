#!/usr/bin/python
# coding=UTF-8
#классы ООП
import datetime

class Dog():
    """Модель собачки. Гааав!"""
    
    def __init__(self,name,age):
        """инициализируем атрибуты имени и возраста"""
        self.name = name
        self.age = age
        print(self.name.title() + " сказала gav gav gav")
        print("- на собаку посмотрели, как на дуру")
        
    def sit(self):
        """будет садиться по команде"""
        print(self.name.title() + " собака села")
        
    def jamp(self):
        """собака будет прыгать по команде"""
        print(self.name.title() + " собака прыгнула")
    
    def howyear(self):
        print(str(self.age) + " - возраст собаки с кличкой " + self.name.title())

class Client():
    def __init__(self,soname,name,otchestvo,year,month,day):
        self.name = name
        self.soname = soname
        self.otchestvo = otchestvo
        self.year = year
        self.month = month
        self.day = day
        self.true = 1

    def getFio(self):
        """собираем фамилию имя отчество"""
        print(self.soname.title()+ " " + self.name.title() + " " + self.otchestvo.title())
    def getYears(self):
        dataToday = datetime.datetime.now()
        birthDay=datetime.datetime(self.year,self.month,self.day)
        years=dataToday.year-birthDay.year
        if dataToday.month<birthDay.month:
            years=years-1
        elif dataToday.month == birthDay.month:
            if dataToday.day < birthDay.day:
                years=years-1
        print(years)

    def getFioShort(self):
        print((self.soname[0]+self.name[0]+self.otchestvo[0]).upper())

    def setName(self,nick):
        if self.checkData() == 1:
            self.name = nick
            self.true = 0

    def setSoname(self,nick):
        if self.checkData() == 1:
            self.soname = nick
            self.true = 0

    def setOtchestvo(self,nick):
        if self.checkData() == 1:
            self.otchestvo = nick
            self.true = 0

    def checkData(self):
        if self.true == 0:
            print('Данные недавно менялись. Попробуйте позднее')
            return 0
        else:
            return 1


class Car():
    """класс по созданию автомобиля"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 0

    def descriptionName(self):
        """возвращаем описание автомобиля"""
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()
    def read_probeg(self):
        """выводим пробег авто"""
        print("пробег этого авто " + str(self.odometr) + " км")
    def update_odometr(self,km):
        """устанавливаем значение на одометре"""
        if km >= self.odometr:
            self.odometr=km
        else:
            print("не читери сука")
    def inkrement_odometr(self,km):
        """увеличиваем показатель одометра на заданный пробег"""
        self.odometr += km

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




client1 = Client('sultanova','karina','vasilevna',1993,3,16)
client2 = Client('prokopova','lenok','artemovna',1965,7,16)
client1.getFio()
client1.setSoname('Karpova')
client1.getFio()
client1.setName('Evgenia')

client1.getFioShort()
client1.getYears()
client2.getYears()

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
