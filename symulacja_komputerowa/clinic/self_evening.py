import simpy
import random
import numpy


NUM_SEATS = 2
TIME = 5
NEW_PAT = 7
SIM_TIME = 300


class Clinic(object):
    def __init__(self, env, num_seats, time):
        self.env = env
        self.seatA = simpy.Resource(env, num_seats-1)
        self.seatB = simpy.Resource(env, num_seats-1)
        self.seatC = simpy.Resource(env, num_seats-1)
        self.time = time
    def self_registration(self):
        yield self.env.timeout(TIME)


def patient(env, id, clinic, typ):
    global patients
    print('%s calls at %.2f.' % (id, env.now))
    if typ == 'A':
        with clinic.seatA.request() as request:
            yield request
            print('%s got through to A %.2f.' % (id, env.now))
            patients += 1
            yield env.process(clinic.self_registration())
            print('%s hung up at %.2f.' % (id, env.now))
            correct = numpy.random.choice(numpy.array([0,1]), p=[0,1])
            if correct != 1:
                yield request
                print('%s got through to A at %.2f.' % (id, env.now))
                yield env.process(clinic.self_registration())
                print('%s hung up at %.2f.' % (id, env.now))
    elif typ == 'B':
        with clinic.seatB.request() as request:
            yield request
            print('%s got through to B at %.2f.' % (id, env.now))
            patients += 1
            yield env.process(clinic.self_registration())
            print('%s hung up at %.2f.' % (id, env.now))
            correct = numpy.random.choice(numpy.array([0,1]), p=[0,1])
            if correct != 1:
                yield request
                print('%s got through to B at %.2f.' % (id, env.now))
                yield env.process(clinic.self_registration())
                print('%s hung up at %.2f.' % (id, env.now))
    else:
        with clinic.seatC.request() as request:
            yield request
            print('%s got through to C at %.2f.' % (id, env.now))
            patients += 1
            yield env.process(clinic.self_registration())
            print('%s hung up at %.2f.' % (id, env.now))
            correct = numpy.random.choice(numpy.array([0,1]), p=[0,1])
            if correct != 1:
                yield request
                print('%s got through to C at %.2f.' % (id, env.now))
                yield env.process(clinic.self_registration())
                print('%s hung up at %.2f.' % (id, env.now))


def setup(env, num_seats, time, new_pat):
    global patients
    clinic = Clinic(env, num_seats, time)
    for i in range(3):
        typ = random.choice(['A', 'B', 'C'])
        env.process(patient(env, 'Patient %d' % i, clinic, typ))
    patients = 0
    while True:
        yield env.timeout(random.randint(new_pat - 1, new_pat + 1))
        i += 1
        typ = random.choice(['A', 'B', 'C'])
        env.process(patient(env, 'Patient %d' % i, clinic, typ))


random.seed(random.gauss(0,100))
env = simpy.Environment()
env.process(setup(env, NUM_SEATS, TIME, NEW_PAT))
env.run(until=SIM_TIME)
print(f'{patients} patients successfuly made an appointment')
