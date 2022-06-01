import random
from queue import Queue
from matplotlib import pyplot as plt
from collections import defaultdict


class Node:
    def __init__(self, number, typ):
        self.typ = typ
        self.number = number
        self.current_task = None
        self.current_complexity = 0
        self.tasks_done = 0

    def give_task(self, task):
        self.current_task = task
        self.current_complexity = task.complexity

    def has_task(self):
        return self.current_task is not None

    def iterate(self):
        if self.current_complexity > 0:
            self.current_complexity -= 1

        if self.current_complexity == 0 and self.current_task is not None:
            self.current_task = None
            self.tasks_done += 1

    def __str__(self):
        return (self.number, self.typ)


class Task:
    def __init__(self, type, complexity):
        self.type = typ
        self.complexity = complexity


if __name__ == '__main__':
    office_configurations = {
    'office1': [
        Node(1, 'A'),
        Node(2, 'A'),
        Node(3, 'A'),
        Node(4, 'B'),
        Node(5, 'B'),
        Node(6, 'B'),
        Node(7, 'C'),
        Node(8, 'C'),
        Node(9, 'C'),
        Node(10, 'E')
        ],
    'office2': [
        Node(1, 'A'),
        Node(2, 'A'),
        Node(3, 'A'),
        Node(4, 'B'),
        Node(5, 'B'),
        Node(6, 'B'),
        Node(7, 'C'),
        Node(8, 'C'),
        Node(9, 'C')
        ],
    'office3': [
        Node(1, 'A'),
        Node(2, 'A'),
        Node(3, 'B'),
        Node(4, 'B'),
        Node(5, 'C'),
        Node(6, 'C'),
        Node(7, 'E'),
        Node(8, 'E'),
        ]
    }

    elements = 30
    task_list = []
    task_types = ['A', 'B', 'C']
    times = {}
    total_times = defaultdict(int)
    total_times_list = [[], [], []]
    total_times2 = [[], [], []]

    for i in range(elements):
        complexity = random.randint(1, 10)
        typ = random.choice(task_types)
        task_list += [Task(typ, complexity)]

    for office_name, office in office_configurations.items():
        q = Queue()
        for task in task_list:
            q.put(task)

        total_time = 0
        all_clear = False
        while not all_clear or not q.empty():
            all_clear = True
            for window in office:
                if window.has_task():
                    all_clear = False
                elif q.empty():
                    pass
                elif window.typ == q.queue[0].type or window.typ == 'E':
                    window.give_task(q.get())
                window.iterate()
            total_time += 1
    times[office_name] = total_time

    print(f'Times for 3 office types:\n{times}')
    task_lists = []
    for _ in range(100):
        aux = []
        for _ in range(elements):
            complexity = random.randint(1, 10)
            typ = random.choice(task_types)
            aux += [Task(typ, complexity)]
        task_lists += [aux]

    for office_nr, (office_name, office) in enumerate(office_configurations.items()):
        for i in range(100):
            task_list = task_lists[i]
            q = Queue()
            for task in task_list:
                q.put(task)

            total_time = 0
            all_clear = False
            while not all_clear or not q.empty():
                all_clear = True
                for window in office:
                    if window.has_task():
                        all_clear = False
                    elif q.empty():
                        pass
                    elif window.typ == q.queue[0].type or window.typ == 'E':
                        window.give_task(q.get())
                    window.iterate()
                total_time += 1
            total_times2[office_nr].append(total_time)
            total_times[office_nr] += total_time

    total_times_list[1] = total_times['office2']
    total_times_list[2] = total_times['office3']
    print(f'Average times for offices 2: {total_times[1]/100} and 3: {total_times[2]/100}')

    plt.figure()
    bins = max([max(total_times2[1]) - min(total_times2[1]), max(total_times2[2]) - min(total_times2[2])])
    plt.hist(total_times2[1], label='3A 3B 3C', color='green', alpha=0.6)
    plt.hist(total_times2[2], label='2A 2B 2C 2E', color='red', alpha=0.6)
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Quantity')
    plt.title('Average times for offices 2 and 3')
    plt.show()
