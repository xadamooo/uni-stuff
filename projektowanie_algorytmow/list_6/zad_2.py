from zad0 import show_robots, m_robots
from operator import attrgetter


def sort_robots(robots, param):
    return sorted(robots, key=attrgetter(param))


def find_robot(robots, param, param_value, low, high):
    if high >= low:
        mid = (high + low) // 2
        print(f'Znajdujemy sie na indeksie {mid}')
        if param == 'rozdzielczosc':
            if robots[mid].rozdzielczosc == param_value:
                print(f'Znaleziono robota')
                return mid
            elif robots[mid].rozdzielczosc > param_value:
                print(f'Robot moze byc po lewej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, low, mid - 1)
            else:
                print(f'Robot moze byc po prawej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, mid + 1, high)
        elif param == 'typ':
            if robots[mid].typ == param_value:
                print(f'Znaleziono robota')
                return mid
            elif robots[mid].typ > param_value:
                print(f'Robot moze byc po lewej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, low, mid - 1)
            else:
                print(f'Robot moze byc po prawej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, mid + 1, high)
        elif param == 'zasieg':
            if robots[mid].zasieg == param_value:
                print(f'Znaleziono robota')
                return mid
            elif robots[mid].zasieg > param_value:
                print(f'Robot moze byc po lewej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, low, mid - 1)
            else:
                print(f'Robot moze byc po prawej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, mid + 1, high)
        elif param == 'identyfikator':
            if robots[mid].identyfikator == param_value:
                print(f'Znaleziono robota')
                return mid
            elif robots[mid].identyfikator > param_value:
                print(f'Robot moze byc po lewej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, low, mid - 1)
            else:
                print(f'Robot moze byc po prawej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, mid + 1, high)
        elif param == 'masa':
            if robots[mid].masa == param_value:
                print(f'Znaleziono robota')
                return mid
            elif robots[mid].masa > param_value:
                print(f'Robot moze byc po lewej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, low, mid - 1)
            else:
                print(f'Robot jest po prawej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, mid + 1, high)
    else:
        return None

'''
robots = m_robots(10)
param = 'rozdzielczosc'
param_value = [18, 19, 20, 21, 22]
print(f'\nPosortowane wedlug "{param}":')
sorted_robots = sort_robots(robots, param)
show_robots(sorted_robots)
for i in param_value:
    searched_robot_index = find_robot(sorted_robots, param, i, 0, len(robots)-1)
    if searched_robot_index != None:
        r = []
        r.append(sorted_robots[searched_robot_index])
        print(f'Robot o parametrze "{param}" wynoszacym "{i}" znajduje się na indeksie {searched_robot_index} i jest to robot:')
        show_robots(r)
        break
'''
      
