import numpy as np
import matplotlib.pyplot as plt
from trajectory_3d import Trajectory3D
plt.rcParams["figure.figsize"] = (9, 8)
seed = 1000


def plot_kalman_3d(measurements, estimations):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    est_x = []
    est_y = []
    est_z = []
    meas_x = []
    meas_y = []
    meas_z = []
    for i in range(len(estimations)):
        est_x.append(estimations[i][i][0])
        est_y.append(estimations[i][i][1])
        est_z.append(estimations[i][i][2])
        meas_x.append(measurements[i][0])
        meas_y.append(measurements[i][1])
        meas_z.append(measurements[i][2])
    ax.plot3D(est_x, est_y, est_z, 'green', label='Wartosci wyestymowane', alpha=0.5)
    ax.plot3D(meas_x, meas_y, meas_z, 'blue', label='Wartosci rzeczywiste', alpha=0.7)
    plt.legend()
    plt.title('Filtr Kalmana 3D')
    plt.show()


def plot_kalman(measurements, estimations, method):
    x = [interval * i for i in range(len(estimations))]
    y1 = estimations
    y2 = measurements
    plt.scatter(x, measurements, alpha=0.3, s=15)
    plt.scatter(x, estimations, alpha=0.3, s=15)
    plt.plot(x, y1, label='Wartosci wyestymowane')
    plt.plot(x, y2, label='Wartosci rzeczywiste')
    plt.title(method)
    plt.legend()
    plt.show()


def generator(v=2, ac=2, time_steps=100, x0=0):
    positions = []
    vs = []
    acs = []
    position = x0
    i = 0
    for t in range(0, time_steps, interval):
        if i % 10 == 0:
            ac += v * 0.05 * ac * np.random.randint(0, 1)
        distance = (v + ac) / 2
        v += ac
        position = position + distance
        positions.append(position)
        vs.append(v)
        acs.append(ac)
        i += 1
    return positions, vs, acs


def filter_a(pos, x_0=0):
    estimated_positions = []
    estimated_position = x_0
    error = []
    for i, z in enumerate(pos, 1):
        z = np.random.normal(z, 0.1)
        gain = 1 / i
        estimated_position = estimated_position + gain * (z - estimated_position)
        estimated_positions.append(estimated_position)
        error.append(abs(z - estimated_position))
    return estimated_positions, error


def filter_ab(pos, x_0=0, v_0=2):
    estimated_positions = []
    estimated_velocities = []
    alpha = 0.2
    beta = 0.1
    error = []
    estimated_position = x_0 + interval * v_0
    estimated_velocity = v_0
    for i, z in enumerate(pos, 1):
        z = np.random.normal(z, 0.1)
        estimated_velocity = estimated_velocity + beta * ((z - estimated_velocity) / interval)
        estimated_position = estimated_position + alpha * (z - estimated_position)
        estimated_positions.append(estimated_position)
        estimated_velocities.append(estimated_velocity)
        error.append(abs(z - estimated_position))
    return estimated_positions, error


def filter_aby(pos, x0=0, v_0=2, ac_0=2):
    estimated_positions = []
    estimated_velocities = []
    estimated_accelerations = []
    alpha = 0.5
    beta = 0.5
    gamma = 0.5
    error = []
    estimated_position = x0 + interval * v_0 + ac_0 * (0.5 * interval * interval)
    estimated_velocity = v_0 + interval * ac_0
    estimated_acceleration = ac_0
    for i, z in enumerate(pos, 1):
        z = np.random.normal(z, 0.1)
        estimated_position = estimated_position + alpha * (z - estimated_position)
        estimated_velocity = estimated_velocity + beta * ((z - estimated_velocity) / interval)
        estimated_acceleration = estimated_acceleration + gamma * (
                    (z - estimated_position) / (0.5 * interval * interval))
        estimated_position = estimated_position + estimated_velocity * interval + (
                    estimated_acceleration * ((interval * interval) / 2))
        estimated_velocity = estimated_velocity + estimated_acceleration * interval
        estimated_positions.append(estimated_position)
        estimated_velocities.append(estimated_velocity)
        estimated_accelerations.append(estimated_accelerations)
        error.append(abs(z - estimated_position))
    return estimated_positions, error


def filter_kalman(pos, x_0=0, v_0=2, ac_0=2):
    estimated_positions = []
    estimated_position = x_0 + interval * v_0 + ac_0 * (0.5 * interval * interval)
    process_noise = 0.5
    extrapolate = 0.5
    error = []
    covariance = process_noise
    for i, z in enumerate(pos, 1):
        z = np.random.normal(z, 0.1)
        covariance += process_noise
        kalman_reinforcement = covariance / (covariance + extrapolate)
        estimated_position = estimated_position + kalman_reinforcement * (z - estimated_position)
        estimated_positions.append(estimated_position)
        covariance = (1 - kalman_reinforcement * covariance)
        error.append(abs(z - estimated_position))
    return estimated_positions, error


def filter_kalman_3d(Z, x_0=(0, 0, 0), v_0=(0, 0, 2), a_0=(1, 0, 2), r=0.5):
    error = []
    N = np.shape(Z)[0]
    X = np.zeros(shape=(N, N, 3))
    V = np.zeros(shape=(N, N, 3))
    A = np.zeros(shape=(N, N, 3))
    p_X = np.zeros(shape=(N, N, 3))
    p_V = np.zeros(shape=(N, N, 3))
    p_A = np.zeros(shape=(N, N, 3))
    p_X[0][0] = r
    p_V[0][0] = r
    p_A[0][0] = r
    X[0][0] = x_0
    V[0][0] = v_0
    A[0][0] = a_0
    dt = 1
    for i in range(N-1):
        n = i
        X[n+1][n], V[n+1][n], A[n+1][n], p_X[n+1][n], p_V[n+1][n], p_A[n+1][n] = X[n][n] + dt*V[n][n] + dt**2 * A[n][n] / 2, \
                                                                                 V[n][n] + dt*A[n][n], \
                                                                                 A[n][n], \
                                                                                 p_X[n][n] + dt*p_V[n][n] + dt**2 * p_A[n][n] / 2, \
                                                                                 p_V[n][n] + dt*p_A[n][n], p_A[n][n]
        n += 1
        K_X = p_X[n][n-1] / (p_X[n][n-1] + r)
        K_V = p_V[n][n-1] / (p_V[n][n-1] + r)
        K_A = p_A[n][n-1] / (p_A[n][n-1] + r)
        X[n][n], V[n][n], A[n][n], p_X[n][n], p_V[n][n], p_A[n][n] = X[n][n-1] + K_X * (Z[n] - X[n][n-1]),\
                                                                     V[n][n-1] + K_V * ((Z[n] - X[n][n-1]) / dt),\
                                                                     A[n][n-1] + K_A * ((Z[n] - X[n][n-1]) / (0.5 * dt**2)),\
                                                                     (1 - K_X) * p_X[n][n-1],\
                                                                     (1 - K_V) * p_V[n][n-1],\
                                                                     (1 - K_A) * p_A[n][n-1]
        error.append(abs(Z[n]-X[n][n]))
    return X, error


if __name__ == "__main__":
    interval = 1
    measured_positions, vs, acs = generator()
    obj3d = Trajectory3D(2, 1)
    measured_positions_3d, N = obj3d.start_values([0, 0, 0], [1, 2, 3], [1, 0, 5], 100)

    a_estimated_position, error_a = filter_a(measured_positions)
    ab_estimated_position, error_ab = filter_ab(measured_positions)
    aby_estimated_positions, error_aby = filter_aby(measured_positions)
    kalman_estimated_positions, error_kalman = filter_kalman(measured_positions)
    kalman_estimated_positions_3d, error3d = filter_kalman_3d(measured_positions_3d)

    plot_kalman(measured_positions, a_estimated_position, 'Filtr alpha')
    plot_kalman(measured_positions, ab_estimated_position, 'Filtr alpha-beta')
    plot_kalman(measured_positions, aby_estimated_positions, 'Filtr alpha-beta-gamma')
    plot_kalman(measured_positions, kalman_estimated_positions, 'Filtr Kalmana')
    plot_kalman_3d(measured_positions_3d, kalman_estimated_positions_3d)

    for i in range(len(error3d)):
        error3d[i] = np.mean(error3d[i])

    print(f'Błąd bezwzgledny dla filtru a: {np.mean(error_a)}\nfiltru a-b: {np.mean(error_ab)}'
          f' filtru a-b-y: {np.mean(error_aby)}\nfiltru Kalmana: {np.mean(error_kalman)}'
          f' filtru Kalmana 3D:{np.mean(error3d)}')