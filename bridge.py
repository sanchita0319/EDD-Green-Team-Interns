import math

def next_theta(,d,t,m,b_inertia):
    theta = 0
    w =0
    count = 0
    while count <=10:
        torque = 9.8 * m * math.cos(theta) * d
        t_inertia = b_inertia + m * d ** 2
        acc = t_inertia / torque
        w = w + acc * t
        theta = theta + 1/2 * acc * t**2 + w*t
        print (theta)
        count += 1

next_theta(10, 0.1, 20, 30)
