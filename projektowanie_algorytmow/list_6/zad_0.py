import random
import string
import json


file = 'D:\\PWR\\Visual Studio\\projektowanie_algorytmow\\list_6\\robots.txt'


class Robot:
    def __init__(self, identyfikator, typ, masa, zasieg, rozdzielczosc):
        self.identyfikator = identyfikator
        self.typ = typ
        self.masa = masa
        self.zasieg = zasieg
        self.rozdzielczosc = rozdzielczosc

    def __getitem__(self, element):
        if element=='masa':
            return self.masa
        elif element=='typ':
            return self.typ
        elif element=='zasieg':
            return self.zasieg
        elif element=='rozdzielczosc':
            return self.rozdzielczosc


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


def show_robots(robots):
    for i in robots:
        print(i.identyfikator, i.typ, i.masa, i.zasieg, i.rozdzielczosc)


def saveload_robots(file, robots, action):
    if action == 'save':
        with open(file, 'w') as f:
            for i in robots:
                json.dump((i.identyfikator, i.typ, i.masa, i.zasieg, i.rozdzielczosc), f, indent=2)
    elif action == 'load':
        with open(file, 'r') as f:
            print(f.read())

