from nltk.corpus import movie_reviews
from nltk import edit_distance, FreqDist
from multiprocessing import Pool
from bloom_filter2 import BloomFilter
from itertools import repeat
import time
import operator


def check_base(word, base):
    if word not in base and word.isalpha():
        return word


def bloom(text):
    with Pool(4) as p:
        start_time = time.time()
        correct = text[:10000]
        bloom_filter = BloomFilter(max_elements=len(correct), error_rate=0.1)
        for i in correct:
            bloom_filter.add(i)
        a = list(filter(lambda x: x is not None, p.starmap(check_base, zip(list(text[10000:]), repeat(bloom_filter)))))
        exec = time.time() - start_time
    print(f'Czas wykonania za pomoca filtru Blooma: {exec}')
    return a


def naive(text):
    with Pool(4) as p:
        start_time = time.time()
        correct = text[:10000]
        a = list(filter(lambda x: x is not None, p.starmap(check_base, zip(list(text[10000:]), repeat(list(correct))))))
        exec = time.time() - start_time
    print(f'Czas wykonania za pomoca podejscia naiwnego: {exec}')
    return a


def top10(a, dict):
    k = 0
    top = []
    for i in dict.keys():
        if i in a and k <= 10:
            k += 1
            top.append(i)
        elif k > 10:
            break
    return top


def levenshtein(top, dict):
    distances = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    for index1, i in enumerate(distances):
        for k in dict.keys():
            if k.isalpha() and len(k) > 1:
                distances[index1][k] = edit_distance(top[index1], k)
    for index, i in enumerate(distances):
        sorted_d = sorted(i.items(), key=operator.itemgetter(1))
        print(f'Dla wyrazu {top[index]} wyrazy najbardziej podobne to: {sorted_d[1:4]}')


if __name__ == '__main__':
    base = movie_reviews.words()
    a = bloom(base)
    b = naive(base)
    dict = dict(FreqDist(base).most_common(len(base)))
    top = top10(a, dict)
    print(f'10 slow najczesciej oznaczonych jako niepoprawne:\n{top}')
    levenshtein(top, dict)
