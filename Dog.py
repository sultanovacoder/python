# coding=UTF-8
class Dog():
    """Модель собачки. Гааав!"""

    def __init__(self,name,age):
        print('Завели новую собаку')
        """инициализируем атрибуты имени и возраста"""
        self.name = name
        self.age = age
        print(self.getName() + " сказала gav gav gav")
        print("- на собаку посмотрели, как на дуру")

    def sit(self):
        """будет садиться по команде"""
        print(self.name.title() + " собака села")

    def jamp(self):
        """собака будет прыгать по команде"""
        print(self.name.title() + " собака прыгнула")

    def howyear(self):
        print(str(self.age) + " - возраст собаки с кличкой " + self.name.title())

    def getName(self):
        return self.name.title()