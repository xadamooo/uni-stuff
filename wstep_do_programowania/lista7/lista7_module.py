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


def Greeting(greeting_index):
    greetings = ['Witaj,', 'Siemanko,', 'Dzien dobry,', 'Hej,']
    return(greetings[greeting_index])
