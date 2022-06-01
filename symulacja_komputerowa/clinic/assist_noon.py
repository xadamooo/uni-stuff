import simpy
import random


NUM_SEATS = 4
TIME = random.randint(2,5)
NEW_PAT = random.randint(3,5)
SIM_TIME = 300


class Clinic(object):
    def __init__(self, env, num_seats, time):
        self.env = env
        self.seat = simpy.Resource(env, num_seats)
        self.time = time
    def assist_registration(self):
        yield self.env.timeout(TIME)


def patient(env, id, clinic):
    global patients
    print('%s calls at %.2f.' % (id, env.now))
    with clinic.seat.request() as request:
        yield request
        print('%s got through %.2f.' % (id, env.now))
        patients += 1
        yield env.process(clinic.assist_registration())
        print('%s hung up at %.2f.' % (id, env.now))


def setup(env, num_seats, time, new_pat):
    global patients
    clinic = Clinic(env, num_seats, time)
    for i in range(4):
        env.process(patient(env, 'Patient %d' % i, clinic))
    patients = 0
    while True:
        yield env.timeout(random.randint(new_pat - 1, new_pat + 1))
        i += 1
        env.process(patient(env, 'Patient %d' % i, clinic))


random.seed(random.gauss(0,100))
env = simpy.Environment()
env.process(setup(env, NUM_SEATS, TIME, NEW_PAT))
env.run(until=SIM_TIME)
print(f'{patients} patients successfuly made an appointment')