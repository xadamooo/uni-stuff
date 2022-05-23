import random
import pandas as pd
import numpy as np
import string

class Robot:
    def __init__(self, id, typ, masa, zas, roz):
        self.id = id
        self.typ = typ
        self.masa = masa
        self.zas = zas
        self.roz = roz

    def __getitem__(self, element):
        if element=='masa':
            return self.masa
        elif element =='typ':
            return self.typ
        elif element=='zasieg':
            return self.zasieg
        elif element=='rozdzielczosc':
            return self.rozdzielczosc

    def save_robot(self):
        robot = {
            'id': self.id,
            'typ': self.typ,
            'masa': self.masa,
            'roz': self.roz,
            'zas': self.zas
        }
        return robot


def create_robot():
    bot = Robot(
        id=''.join(random.choices(string.ascii_letters + string.digits, k=3)),
        typ=random.choice(['AUV', 'AFV', 'AGV']),
        masa=np.random.randint(50, 2000),
        zas=np.random.randint(1, 1000),
        roz=np.random.randint(1, 30)
    )
    return bot


def create_m_bots(m):
    bots = list()
    for _ in range(m):
        bots.append(create_robot())
    return bots


botslist = create_m_bots(10)
df = pd.DataFrame()
for b in botslist:
    df = df.append(b.save_robot(), ignore_index=True)


def save_to_file(data):
    data.to_csv('pliki/roboty.csv')


def read_from_file(path):
    data = pd.read_csv(path)
    return data