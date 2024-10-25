class Foydalanuvchi:
    def __init__(self, login, parol):
        self.log = login
        self.par = parol

class Admin(Foydalanuvchi):
    def __init__(self, login, parol):
        super().__init__(login, parol)

    def ban_user(self, foydalanuvchi, ls):
        if foydalanuvchi in ls:
            ls.remove(foydalanuvchi)
            print(f"{foydalanuvchi.log} foydalanuvchi ban berildi.")
        else:
            print("Unday foydalanuvchi yo'q!!!")

foydalanuvchi1 = Foydalanuvchi('Shohruz', '456joker67@')
foydalanuvchi2 = Foydalanuvchi('Abdulhamid07', "metro6789@")
foydalanuvchi3 = Foydalanuvchi('Nodir', '13erta#2')
foydalanuvchi4 = Foydalanuvchi('Gopnik', '9087kole@')

ls = [foydalanuvchi1, foydalanuvchi2, foydalanuvchi3, foydalanuvchi4]

admin = Admin('Admin_007', 'banlove#')

admin.ban_user(foydalanuvchi2, ls)
admin.ban_user(foydalanuvchi3, ls)
admin.ban_user(foydalanuvchi2, ls)


# for i in ls:
#     print('Foydalanuvchilar login:',i.log,'va paroli:',i.par)



