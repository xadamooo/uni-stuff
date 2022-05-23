from zad4_0 import *


def quick_sort_desc(arr, low, high):
    if low >= high or high >= len(arr):
        return
    p, arr = partition_desc(arr, low, high)
    quick_sort_desc(arr, low, p - 1)
    quick_sort_desc(arr, p + 1, high)
    return arr


def partition_desc(arr, low, high):
    piv = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= piv:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i, arr


def quick_sort(arr, low, high):
    if low > high or low < 0:
        return
    p, arr = partition(arr, low, high)
    quick_sort(arr, low, p - 1)
    quick_sort(arr, p + 1, high)
    return arr


def partition(arr, low, high):
    piv = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= piv:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i, arr


def sort_robots(bots, feat, kind=0):
    flist = [b[feat] for b in bots]
    if kind == 0:
        flist = quick_sort(flist, 0, len(flist) - 1)
    elif kind == 1:
        flist = quick_sort_desc(flist, 0, len(flist) - 1)
    elif kind == 2:
        flist = [str(n) for n in flist]
        flist = quick_sort(flist, 0, len(flist) - 1)
    new_robots = list()
    for r in flist:
        for bot in bots:
            if bot[feat] == r:
                new_robots.append(bot)
                bots.remove(bot)
    return new_robots


vector = create_m_bots(20)
vector = [b.save_robot() for b in vector]
feature = 'roz'
robots = sort_robots(vector, feat=feature)
for r in robots:
    print(r)


'''
vector = create_m_bots(100)
vector = [b.save_robot() for b in vector]
# 0 - rosnaco, 1 - malejaco, 2 - alfabetycznie
features = {
            'typ': 2,
            'roz': 1,
            'masa': 0
            }
feat_list = list(features.keys())
feat_list.reverse()
for f in feat_list:
    vector = sort_robots(bots=vector, feat=f, kind=features[f])
for r in vector:
    print(r)
'''
