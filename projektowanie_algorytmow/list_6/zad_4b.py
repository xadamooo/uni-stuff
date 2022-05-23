from zad0 import show_robots, m_robots
from zad2 import sort_robots

def find_robot(robots, param, param_value, low, high):
    if high >= low:
        a, b = param_value
        mid = (high + low) // 2
        print(f'Znajdujemy sie na indeksie {mid}')
        if param == 'rozdzielczosc':
            if robots[mid].rozdzielczosc <= b and robots[mid].rozdzielczosc >= a:
                print(f'Znaleziono robota')
                return mid, low, high
            elif robots[mid].rozdzielczosc > b:
                print(f'Robot moze byc po lewej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, low, mid - 1)
            else:
                print(f'Robot moze byc po prawej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, mid + 1, high)
        elif param == 'typ':
            if robots[mid].typ <= b and robots[mid].typ >= a:
                print(f'Znaleziono robota')
                return mid
            elif robots[mid].typ > b:
                print(f'Robot moze byc po lewej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, low, mid - 1)
            else:
                print(f'Robot moze byc po prawej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, mid + 1, high)
        elif param == 'zasieg':
            if robots[mid].typ <= b and robots[mid].zasieg >= a:
                print(f'Znaleziono robota')
                return mid
            elif robots[mid].zasieg > b:
                print(f'Robot moze byc po lewej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, low, mid - 1)
            else:
                print(f'Robot moze byc po prawej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, mid + 1, high)
        elif param == 'identyfikator':
            if robots[mid].identyfikator <= b and robots[mid].identyfikator >= a:
                print(f'Znaleziono robota')
                return mid
            elif robots[mid].identyfikator > b:
                print(f'Robot moze byc po lewej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, low, mid - 1)
            else:
                print(f'Robot moze byc po prawej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, mid + 1, high)
        elif param == 'masa':
            if robots[mid].masa <= b and robots[mid].masa >= a:
                print(f'Znaleziono robota')
                return mid
            elif robots[mid].masa > b:
                print(f'Robot moze byc po lewej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, low, mid - 1)
            else:
                print(f'Robot jest po prawej stronie od indeksu {mid}')
                return find_robot(robots, param, param_value, mid + 1, high)
    else:
        return None


def lower(low, high, robots, param, param_value):
    a, b = param_value
    while (low < high):
        mid = low + (high - low) // 2
        if param == 'rozdzielczosc':
            if robots[mid].rozdzielczosc < b and robots[mid].rozdzielczosc > a:
                low = mid + 1
            else:
                high = mid
        elif param == 'typ':
            if robots[mid].typ < b and robots[mid].typ > a:
                low = mid + 1
            else:
                high = mid
        elif param == 'zasieg':
            if robots[mid].zasieg < b and robots[mid].zasieg > a:
                low = mid + 1
            else:
                high = mid
        elif param == 'identyfikator':
            if robots[mid].identyfikator < b and robots[mid].identyfikator > a:
                low = mid + 1
            else:
                high = mid
        elif param == 'masa':
            if robots[mid].masa < b and robots[mid].masa > a:
                low = mid + 1
            else:
                high = mid
    return low


def upper(low, high, robots, param, param_value):
    a, b = param_value
    while(low < high):
        mid = low + (high - low) // 2
        if param == 'rozdzielczosc':
            if robots[mid].rozdzielczosc < b and robots[mid].rozdzielczosc > a:
                high = mid
            else:
                low = mid + 1
        elif param == 'typ':
            if robots[mid].typ < b and robots[mid].typ > a:
                high = mid
            else:
                low = mid + 1
        if robots[mid].zasieg < b and robots[mid].zasieg > a:
            if robots[mid].zasieg > param_value:
                high = mid
            else:
                low = mid + 1
        elif param == 'identyfikator':
            if robots[mid].identyfikator < b and robots[mid].identyfikator > a:
                high = mid
            else:
                low = mid + 1
        elif param == 'masa':
            if robots[mid].masa < b and robots[mid].masa > a:
                high = mid
            else:
                low = mid + 1
    return low


param = 'rozdzielczosc'
param_value = (20, 22)
robots = m_robots(40)
sorted = sort_robots(robots, param)
show_robots(sorted)
a = find_robot(sorted, param, param_value, 0, len(robots)-1)
try:
    mid, low, high = a
    final_low = lower(low, mid, sorted, param, param_value)
    final_up = upper(mid, high, sorted, param, param_value)
    print(final_low, final_up)
except TypeError:
    print(a)
