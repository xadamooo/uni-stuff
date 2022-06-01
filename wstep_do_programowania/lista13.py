from math import sqrt


def format_bytes(x):
    unit = 1024
    a = int(x)//(unit**3)
    b = (int(x) % unit**3)//(unit**2)
    c = (int(x) % unit**2)//unit
    d = (int(x) % unit)
    print(f'ZAD1:\n{a}GB + {b}MB + {c}KB + {d}B')


value = [i for i in range(0, 51)]
filtered = list(filter(lambda value: value % 3 == 0 or value % 5 == 0, value))


def normalize(values):
    sum_root = sqrt(sum([x*x for x in values]))
    return [x/sum_root for x in values]


'''1'''
format_bytes(9876543210)
'''2'''
print(f'ZAD2:\n{filtered}')
'''3'''
print('ZAD3:')
for n in normalize((2.2, 5.6, 4.3, 3.0, 0.5)):
    print('%.5f' % n, ' ')
