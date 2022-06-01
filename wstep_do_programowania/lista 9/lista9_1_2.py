import pickle


def add_note():
    diary[input("PODAJ DZIEŃ: ")] = input("DODAJ WPIS: ")


def save_note():
    pickle.dump(diary, open('diary.p', 'wb'))


try:
    diary = pickle.load(open('diary.p', 'rb'))
except FileNotFoundError:
    diary = {}

add_note()
save_note()
