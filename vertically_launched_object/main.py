import numpy as np
import matplotlib.pyplot as plt

def height_of_ball(time: np.ndarray, initial_velocity=5, gravity=9.81):
    """Calculate the height of a ball at a given time.

    :param time: Time in seconds.
    :param initial_velocity: Initial velocity in m/s (default is 5 m/s).
    :param gravity: Acceleration due to gravity in m/s^2 (default is 9.81 m/s^2).

    :return: Height of the ball in meters.
    """
    return initial_velocity * time - 0.5 * gravity * time ** 2

def max_height(heights: np.ndarray):
    max_height = heights[0]
    max_idx = 0

    for idx, height in enumerate(heights):
        if height > max_height:
            max_height = height
            max_idx = idx

    return max_height, max_idx

def derivative(time: np.ndarray, initial_velocity=5, gravity=9.81) -> np.ndarray:
    return initial_velocity - gravity * time

if __name__ == '__main__':
    times = np.linspace(0, 2, 2000)
    heights = height_of_ball(times)
    y_max, idx_max = max_height(heights)
    time_at_max_height = times[idx_max]
    dy_dt = derivative(times)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 14))

    # plt.figure(figsize=(7, 4))

    ax1.plot(times, heights, linewidth=2, color='black')
    ax1.plot(time_at_max_height, y_max, marker='*', markersize=14, color='red')
    ax1.set_title("Vertical Trajectory y(t) for v0=5 m/s, g=9.81 m/s²")
    ax1.set_xlabel("Time t (s)")
    ax1.set_ylabel("Height y (m)")
    ax1.grid(True)

    ax2.plot(times, dy_dt, linewidth=2, color='black')
    ax2.set_title("Velocity dy/dt vs. Time")
    ax2.set_xlabel("Time t (s)")
    ax2.set_ylabel("dy/dt (m/s)")
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

# The derivative plot reveals the continuous deceleration under gravity, the
# momentary stop at the peak (v = 0), and the acceleration back downward — a
# perfect illustration of motion under constant acceleration.



