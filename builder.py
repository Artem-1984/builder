from abc import ABCMeta


class Phone:
    def __init__(self):
        self.data: str = ''

    def about_phone(self) -> str:
        return self.data

    def append_data(self, string: str):
        self.data += string


class IDeveloper(metaclass=ABCMeta):
    def creater_display(self):
        pass

    def creater_box(self):
        pass

    def system_install(self):
        pass

    def get_phone(self) -> Phone:
        pass


class IphoneDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()

    def creater_display(self):
        self.__phone.append_data("Произведен дисплей Iphone ")

    def creater_box(self):
        self.__phone.append_data("Произведен корпус Iphone ")

    def system_install(self):
        self.__phone.append_data("Установлена система Iphone ")

    def get_phone(self) -> Phone:
        return self.__phone


class AndroidDevelop(IDeveloper):
    def __init__(self):
        self.__phone = Phone()

    def creater_display(self):
        self.__phone.append_data("Произведен дисплей Samsung ")

    def creater_box(self):
        self.__phone.append_data("Произведен корпус Samsung ")

    def system_install(self):
        self.__phone.append_data("Установлена система Android ")

    def get_phone(self) -> Phone:
        return self.__phone


class Director:
    def __init__(self, devoloper: IDeveloper):
        self.__devoloper = devoloper

    def set_developer(self, devoloper: IDeveloper):
        self.__devoloper = devoloper

    def mount_only_phone(self) -> Phone:
        self.__devoloper.creater_box()
        self.__devoloper.creater_display()
        return self.__devoloper.get_phone()

    def mount_full_phone(self) -> Phone:
        self.__devoloper.creater_box()
        self.__devoloper.creater_display()
        self.__devoloper.system_install()
        return self.__devoloper.get_phone()


if __name__ == '__main__':
    android_developer: IDeveloper = AndroidDevelop()

    director = Director(android_developer)

    samsung: Phone = director.mount_full_phone()
    print(samsung.about_phone())

    iphone_developer: IDeveloper = IphoneDeveloper()
    director.set_developer(iphone_developer)

    iphone: Phone = director.mount_full_phone()
    print(iphone.about_phone())




class Pasta:
    def __init__(self):
        self.data: str = ''

    def what_pasta(self) -> str:
        return self.data

    def append_data(self,string: str):
        self.data +=string

class Chief(metaclass=ABCMeta):
    def type_of_paste(self):
        pass
    def sauce(self):
        pass
    def filling(self):
        pass
    def additives(self):
        pass
    def get_pasta(self) -> Pasta:
        pass

class Capellini(Chief):
    def __init__(self):
        self.__pasta = Pasta()

    def type_of_paste(self):
        self.__pasta.append_data(" тонкие ")
    def sauce(self):
        self.__pasta.append_data(' томатный соус ')
    def filling(self):
        self.__pasta.append_data(' Макароны ')
    def additives(self):
        self.__pasta.append_data(' помидорки ')

    def get_pasta(self) -> Pasta:
        return self.__pasta

class Carbonara(Chief):
    def __init__(self):
        self.__pasta = Pasta()

    def type_of_paste(self):
        self.__pasta.append_data( "ну паста ")
    def sauce(self):
        self.__pasta.append_data(' сливки с сырок ')
    def filling(self):
        self.__pasta.append_data(' бекон ')
    def additives(self):
        self.__pasta.append_data(' яйчный желток ')

    def det_pasta(self) -> Pasta:
        return self.__pasta

class Campanella(Chief):
    def __init__(self):
        self.__pasta = Pasta()

    def type_of_paste(self):
        self.__pasta.append_data(" короткая паста ")
    def sauce(self):
        self.__pasta.append_data(' томатный соус ')
    def filling(self):
        self.__pasta.append_data(' грибы ')
    def additives(self):
        self.__pasta.append_data(' сыр ')

    def det_pasta(self) -> Pasta:
        return self.__pasta


class Director:
    def __init__(self,chief: Chief):
        self.__chief = chief
    def set_chief(self,chief: Chief):
        self.__chief = chief

    def cook_pasta(self) -> Pasta:
        self.__chief.sauce()
        self.__chief.filling()
        self.__chief.additives()
        self.__chief.type_of_paste()
        return self.__chief.get_pasta()

if __name__ == '__main__':
    x : Chief = Carbonara()
    director = Director(x)
