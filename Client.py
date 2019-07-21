class Client():
    def __init__(self,soname,name,otchestvo,year,month,day):
        self.name = name
        self.soname = soname
        self.otchestvo = otchestvo
        self.year = year
        self.month = month
        self.day = day
        self.true = 1
        print('Занесение нового клиента в базу, - ' + self.getFio() + " " + str(self.day) +"." + str(self.month) + "."+ str(self.year) + " ("+self.getYears()+")")

    def getFio(self):
        """собираем фамилию имя отчество"""
        self.fio = self.soname.title()+ " " + self.name.title() + " " + self.otchestvo.title()
        return self.fio
    def getYears(self):
        dataToday = datetime.datetime.now()
        birthDay=datetime.datetime(self.year,self.month,self.day)
        years=dataToday.year-birthDay.year
        if dataToday.month<birthDay.month:
            years=years-1
        elif dataToday.month == birthDay.month:
            if dataToday.day < birthDay.day:
                years=years-1
        return str(years)

    def getFioShort(self):
        print((self.soname[0]+self.name[0]+self.otchestvo[0]).upper())

    def setName(self,nick):
        if self.checkData() == 1:
            print("\nДанные пользователя изменились " + "\nбыло "+ self.getFio() + " ->")
            self.name = nick
            self.true = 0
            print("стало " + self.getFio()+"\n")


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
            print(self.getFio() + ': Попытка изменения персональных данных, которые недавно менялись. Попробуйте позднее')
            return 0
        else:
            return 1

    def kormitDog(self,dogName):
        print("клиент " + self.getFio() + " кормит собаку " + dogName.getName())