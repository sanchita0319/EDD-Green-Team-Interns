import math
# d = distance between center of bridge and robot
# t = seconds at which measurement is being taken after initation
# m = mass of groundbot
#b_intertia = inertia of the bridge
#theta = angle in rad
distance = []
mass = []
def distance_mass(distance, mass):
  total = 0
  for i in distance:
    total += i
  print (total)
  global d 
  d = total
  sum = 0
  for i in mass:
    sum += i
  total1 = sum / len(mass)
  print (total1)
  global m
  m = total1
  
theta = 0

def next_theta(d,m,theta,b_inertia,t):
    w =0
    torque = 9.8 * m * math.cos(theta) * d
    t_inertia = b_inertia + m * d ** 2
    acc = t_inertia / torque
    w = w + acc * t
    theta = theta + 1/2 * acc * t**2 + w*t
    print (theta)
    global theta1
    theta1 = theta
 
