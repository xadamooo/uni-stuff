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


def generate_robot(n=4, typ=['AUV', 'AFV', 'AGV']):
    identyfikator = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
    typ = random.choice(typ)
    masa = random.randint(50, 2000)
    zasieg = random.randint(1, 1000)
    rozdzielczosc = random.randint(1, 30)
    return identyfikator, typ, masa, zasieg, rozdzielczosc


def m_robots(m):
    robots = []
    for _ in range(m):
        identyfikator, typ, masa, zasieg, rozdzielczosc = generate_robot()
        robots.append(Robot(identyfikator, typ, masa, zasieg, rozdzielczosc))
    return robots


def save_to_file(data):
    data.to_csv('pliki/roboty.csv')


def read_from_file(path):
    data = pd.read_csv(path)
    return data