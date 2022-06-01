import random
'''zad1'''


class Restauracja:
    def __init__(self, restaurant_name, restaurant_type, served_clients=0):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.served_clients = served_clients

    def opis_restauracji(self):
        print('Nazwa restauracji:', self.restaurant_name,
              '\nTyp restauracji:', self.restaurant_type,
              '\nObsluzonych klientow:', self.served_clients)

    def otwarta_restauracja(self):
        if currentDay >= 0 and currentDay <= 4:
            print('Restauracja jest otwarta\n')
        else:
            print('Restauracja jest zamknieta\n')

    def ustaw_liczbe_obsluzonych_klientow(self, new_served):
        self.served_clients = new_served

    def dodaj_liczbe_obsluzonych_klientow(self, added_served):
        self.served_clients = self.served_clients + added_served


def Date(currentDay):
    days = [
        'Poniedzialek',
        'Wtorek',
        'Sroda',
        'Czwartek',
        'Piatek',
        'Sobota',
        'Niedziela']
    print('Dzis jest:', days[currentDay], '\n')


currentDay = random.randint(0, 6)
Date(currentDay)
restaurant_1 = Restauracja('Rzymskie Wakacje', 'wloska')
restaurant_2 = Restauracja('Orientalna', 'tajska')
restaurant_3 = Restauracja('Manekin', 'amerykanska')
restaurant_1.opis_restauracji()
restaurant_1.otwarta_restauracja()
restaurant_2.opis_restauracji()
restaurant_2.otwarta_restauracja()
restaurant_3.opis_restauracji()
restaurant_3.otwarta_restauracja()
restaurant_1.ustaw_liczbe_obsluzonych_klientow(115)
restaurant_2.ustaw_liczbe_obsluzonych_klientow(234)
restaurant_3.ustaw_liczbe_obsluzonych_klientow(96)
restaurant_1.dodaj_liczbe_obsluzonych_klientow(10)
restaurant_2.dodaj_liczbe_obsluzonych_klientow(5)
restaurant_3.dodaj_liczbe_obsluzonych_klientow(12)
restaurant_1.opis_restauracji()
restaurant_1.otwarta_restauracja()
restaurant_2.opis_restauracji()
restaurant_2.otwarta_restauracja()
restaurant_3.opis_restauracji()
restaurant_3.otwarta_restauracja()


class Lodziarnia(Restauracja):
    def __init__(self, restaurant_name, restaurant_type, served_clients=0):
        super().__init__(restaurant_name, restaurant_type, served_clients)
        self.smaki = ['truskawowy', 'czekoladowy', 'waniliowy']

    def flavors(self):
        print('Smaki lodow:', self.smaki)


icecream_shop = Lodziarnia('Sopelek', 'lodziarnia')
icecream_shop.opis_restauracji()
icecream_shop.flavors()

'''zad2'''


print("\n")


class Uzytkownik:
    def __init__(self, first_name, last_name, login_attempts,
                 password, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.password = password
        self.date_of_birth = date_of_birth

    def opisz_uzytownika(self):
        print('Imie:', self.first_name,
              '\nNazwisko:', self.last_name,
              '\nProby logowania:', self.login_attempts,
              '\nHaslo:', self.password,
              '\nData urodzenia:', self.date_of_birth)

    def pozdrow_uzytkownika(self, greeting_type):
        print(greeting_type, self.first_name, self.last_name, '\n')

    def dodaj_probe_logowania(self):
        self.login_attempts = self.login_attempts + 1

    def resetuj_proby_logowania(self):
        self.login_attempts = 0


def Greeting(greeting_index):
    greetings = ['Witaj,', 'Siemanko,', 'Dzien dobry,', 'Hej,']
    return(greetings[greeting_index])


user_1 = Uzytkownik('Adam', 'Bednarski', 0, 'haslo123', '2001-05-08')
user_2 = Uzytkownik('Kamil', 'Kowalczyk', 0, 'password321', '2001-03-21')
user_3 = Uzytkownik('Bartosz', 'Pyka', 0, 'haslo321', '2001-11-14')
user_1.dodaj_probe_logowania()
user_1.dodaj_probe_logowania()
user_2.dodaj_probe_logowania()
user_3.dodaj_probe_logowania()
user_3.dodaj_probe_logowania()
user_3.dodaj_probe_logowania()
user_1.opisz_uzytownika()
print('\n')
user_2.opisz_uzytownika()
print('\n')
user_3.opisz_uzytownika()
print('\n')
user_1.resetuj_proby_logowania()
user_2.resetuj_proby_logowania()
user_3.resetuj_proby_logowania()
user_1.opisz_uzytownika()
greeting_index = random.randint(0, 3)
user_1.pozdrow_uzytkownika(Greeting(greeting_index))
user_2.opisz_uzytownika()
greeting_index = random.randint(0, 3)
user_2.pozdrow_uzytkownika(Greeting(greeting_index))
user_3.opisz_uzytownika()
greeting_index = random.randint(0, 3)
user_3.pozdrow_uzytkownika(Greeting(greeting_index))


class Admin(Uzytkownik):
    def __init__(self, first_name, last_name, login_attempts,
                 password, date_of_birth):
        super().__init__(first_name, last_name, login_attempts,
                         password, date_of_birth)
        self.privileges = Przywileje([
            'moze dodac post',
            'moze usunac post',
            'moze zablokowac uzytkownika',
            'moze edytowac dane uzytkownika',
            'moze nadac uprawnienia administratora'])

    def show_privileges(self):
        self.privileges.print_privileges()


class Przywileje:
    def __init__(self, administrator):
        self.privilege = administrator

    def print_privileges(self):
        print('Przywileje: ', self.privilege)


admin_1 = Admin('Admin', 'Admiński', 0, 'haselko312', '2002-10-10')
admin_1.show_privileges()
