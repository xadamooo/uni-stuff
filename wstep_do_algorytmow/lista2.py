import random
import time
from matplotlib import pyplot as plt


def dataset_generator(size, range_begin, range_end):
    dataset = []
    for i in range(size):
        dataset.append(random.randint(range_begin, range_end))
    return dataset


def stopwatch(funct, size, range_begin, range_end):
    dataset = dataset_generator(size, range_begin, range_end)
    start = time.time()
    funct(dataset)
    end = time.time()
    return end - start


def bubble_sort(dataset):
    for i in range(1, len(dataset)-1):
        for j in range(0, len(dataset) - 1):
            if dataset[j] > dataset[j + 1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j + 1] = temp
    return dataset


def bubble_sort_1(dataset):
    for i in range(1, len(dataset) - 1):
        swapped = False
        for j in range(0, len(dataset) - 1):
            if dataset[j] > dataset[j + 1]:
                swapped = True
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j + 1] = temp
        if swapped is False:
            break
    return dataset


def bubble_sort_2(dataset):
    for i in range(0, len(dataset) - 1):
        for j in range(0, len(dataset) - 1 - i):
            if dataset[j] > dataset[j + 1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j + 1] = temp
    return dataset


def insertion_sort(dataset):
    for i in range(len(dataset)):
        for j in range(0, i):
            if dataset[i] < dataset[j]:
                temp = dataset[i]
                dataset[i] = dataset[j]
                dataset[j] = temp
    return dataset


def selection_sort(dataset):
    for i in range(len(dataset)):
        for j in range(i + 1, len(dataset)):
            if dataset[i] > dataset[j]:
                temp = dataset[i]
                dataset[i] = dataset[j]
                dataset[j] = temp
    return dataset


def avg_time(size, loops=10):
    times = [[], [], [], [], []]
    avg_times = []
    for i in range(loops):
        times[0].append(stopwatch(selection_sort, size, 1, 100))
        times[1].append(stopwatch(bubble_sort, size, 1, 100))
        times[2].append(stopwatch(insertion_sort, size, 1, 100))
        times[3].append(stopwatch(bubble_sort_1, size, 1, 100))
        times[4].append(stopwatch(bubble_sort_2, size, 1, 100))
    avg_times.append(sum(times[0]) / loops)
    avg_times.append(sum(times[1]) / loops)
    avg_times.append(sum(times[2]) / loops)
    avg_times.append(sum(times[3]) / loops)
    avg_times.append(sum(times[4]) / loops)
    return avg_times


def max_time(size, loops=10):
    times = [[], [], [], [], []]
    max_times = []
    for i in range(loops):
        times[0].append(stopwatch(selection_sort, size, 1, 100))
        times[1].append(stopwatch(bubble_sort, size, 1, 100))
        times[2].append(stopwatch(insertion_sort, size, 1, 100))
        times[3].append(stopwatch(bubble_sort_1, size, 1, 100))
        times[4].append(stopwatch(bubble_sort_2, size, 1, 100))
    max_times.append(max(times[0]))
    max_times.append(max(times[1]))
    max_times.append(max(times[2]))
    max_times.append(max(times[3]))
    max_times.append(max(times[4]))
    return max_times


print('ŚREDNIE DLUGOSCI DLA KOLEJNO SELECTION SORT, BUBBLE SORT, ZMODYFIKOWANY BUBBLE SORT, ZMODYFIKOWANY INACZEJ BUBBLE SORT I INSERT SORT:\n', avg_time(100))
print('MAKSYMALNE DLUGOSCI DLA KOLEJNO SELECTION SORT, BUBBLE SORT, ZMODYFIKOWANY BUBBLE SORT, ZMODYFIKOWANY INACZEJ BUBBLE SORT I INSERT SORT:\n', max_time(100))

sizes = [10, 20, 50, 100, 250, 500, 1000]
avgs_sel = []
avgs_bubble = []
avgs_bubble1 = []
avgs_bubble2 = []
avgs_ins = []
maxs_sel = []
maxs_bubble = []
maxs_bubble1 = []
maxs_bubble2 = []
maxs_ins = []
for size in sizes:
    avg_times = avg_time(size, 1)
    max_times = max_time(size, 1)
    avgs_sel.append(avg_times[0])
    avgs_bubble.append(avg_times[1])
    avgs_bubble1.append(avg_times[3])
    avgs_bubble2.append(avg_times[4])
    avgs_ins.append(avg_times[2])
    maxs_sel.append(max_times[0])
    maxs_bubble.append(avg_times[1])
    maxs_bubble1.append(max_times[3])
    maxs_bubble2.append(max_times[4])
    maxs_ins.append(max_times[2])


fig1 = plt.figure()
ax1 = plt.subplot()
ax1.plot(sizes, avgs_sel,
         color='blue', label='selection')
ax1.plot(sizes, avgs_bubble,
         color='green', label='bubble')
ax1.plot(sizes, avgs_ins,
         color='red', label='insert')
plt.title('Średni czas pomiaru')
plt.xlabel('Długość ciagu')
plt.ylabel('Czas')
plt.grid(True)
plt.legend(loc="upper left")
plt.show()

fig2 = plt.figure()
ax2 = plt.subplot()
ax2.plot(sizes, maxs_sel,
         color='blue', label='selection')
ax2.plot(sizes, maxs_bubble,
         color='green', label='bubble')
ax2.plot(sizes, maxs_ins,
         color='red', label='insert')
plt.title('Maksymalny czas pomiaru')
plt.xlabel('Długość ciagu')
plt.ylabel('Czas')
plt.grid(True)
plt.legend(loc="upper left")
plt.show()

fig3 = plt.figure()
ax3 = plt.subplot()
ax3.plot(sizes, avgs_bubble,
         color='blue', label='bubble')
ax3.plot(sizes, avgs_bubble1,
         color='green', label='bubble1')
ax3.plot(sizes, avgs_bubble2,
         color='red', label='bubble2')
plt.title('Średni czas pomiaru')
plt.xlabel('Długość ciagu')
plt.ylabel('Czas mierzony w sekundach')
plt.grid(True)
plt.legend(loc="upper left")
plt.show()

fig4 = plt.figure()
ax4 = plt.subplot()
ax4.plot(sizes, maxs_bubble,
         color='blue', label='bubble')
ax4.plot(sizes, maxs_bubble1,
         color='green', label='bubble1')
ax4.plot(sizes, maxs_bubble2,
         color='red', label='bubble2')
plt.title('Maksymalny czas pomiaru')
plt.xlabel('Długość ciagu')
plt.ylabel('Czas mierzony w sekundach')
plt.grid(True)
plt.legend(loc="upper left")
plt.show()
