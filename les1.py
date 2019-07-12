#классы ООП
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
        print(self.name.title() + "собака села")
        
    def jamp(self):
        """собака будет прыгать по команде"""
        print(self.name.title() + "собака прыгнула")
    
    """def howyear(self):
        print(self.age.title() + " возраст собаки с кличкой" + self.name.title()) почему это не работает??"""
        
my_dog = Dog('Topik', 4)
my_dog2 = Dog('Nika',7)

"""my_dog.howyear()"""
my_dog.sit()
my_dog2.jamp()
        
print("Доброе утро, Alina")
print("не ленись!")
print("двумя кнопками мыши назать на файл \"file.py\"!")
answer3 = input("А ты в курсе, что можно запускать питоновский файл напрямую и вводить туда значения? (Y/N)")
if answer3 == 'Y':
    print("умничка")
else:
    print("нихера не умничка")
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