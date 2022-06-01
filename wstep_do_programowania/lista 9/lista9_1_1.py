import pickle

try:
    diary = pickle.load(open('diary.p', 'rb'))
except FileNotFoundError:
    print("Nie znaleziono pliku")
else:
    for note in reversed(diary):
        print(note, diary[note])
