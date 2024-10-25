class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.fanlar = []

    def fanga_yozil(self, fan):
        if isinstance(fan, Fan):
            self.fanlar.append(fan)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            print(f"Siz {fan.fan_nom} faniga yozilmagansiz!")

    def chiqarish(self):
        print(f"Talabaning fanlar: {', '.join(fan.fan_nom for fan in self.fanlar) if self.fanlar else 'Fanlar yo\'q'}")

    def get_info(self):
        info = f'{self.ism} {self.familiya}.'
        info += f' Passport: {self.passport}, {self.tyil}-yilda tugilgan.'
        return info

    def get_age(self, yil):
        return f'Talaba {yil - int(self.tyil)} yoshda.'

class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil):
        super().__init__(ism, familiya, passport, tyil)

class Fan:
    def __init__(self, nom):
        self.fan_nom = nom

Algebra = Fan('Algebra')
Fizika = Fan('Fizika')
Informatika = Fan('Informatika')
Ingliz_tili = Fan('Ingliz tili')
Tarix = Fan('Tarix')
Turk_tili = Fan('Turk tili')

talaba = Talaba('Farux', 'Sodiqov', 'AA563748', '2005')

talaba.fanga_yozil(Algebra)
talaba.fanga_yozil(Informatika)
talaba.fanga_yozil(Ingliz_tili)

talaba.remove_fan(Ingliz_tili)

print(talaba.get_info())
talaba.chiqarish()
print(talaba.get_age(2024))
