import random


def test_fermata(p, k):
    if p == 2:
        return True

    if p % 2 == 0:
        return False

    for _ in range(k):
        q = random.randint(1, p-1)
        if pow(q, p-1) % p != 1:
            return False
    return True


def test_millera_rabina(p, k):
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    r, s = 0, p - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, p - 2)
        x = pow(a, s, p)
        if x == 1 or x == p - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, p)
            if x == p - 1:
                break
        else:
            return False
    return True
