class Car():
    """класс по созданию автомобиля"""
    def __init__(self,make,model,year):
        print('Приобрели новый авто')
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
            print("Попытка открутить значение счетчика: не читери сука")
    def inkrement_odometr(self,km):
        """увеличиваем показатель одометра на заданный пробег"""
        self.odometr += km