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
answer3 = input("А ты в курсе, что можно запускать питоновский файл напрямую и вводить туда значения? (Y/N)")
if answer3 == 'Y':
    print(" умничка")
else:
    print("нихера не умничка%n")
print(name, ", добро пожаловать в мир пайтон")
    
print("\nРегистрация клиента")
class Client():
    def __init__(self,name,soname,otchestvo,year,month,day):
        self.name = name
        self.soname = soname
        self.otchestvo = otchestvo
        self.year = year
        self.month = month
        self.day = day
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

   
client1 = Client('karina','sultanova','vasilevna',1993,7,16)
client1.getFio()
client1.getYears()
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
