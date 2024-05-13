import matplotlib.pyplot as plt 
from math import sin, asin, tan, pi

run_time = 5
delta = 0.001

friction_force = 0.013
ramp_length = 1.56
ramp_height = 0.72
ramp_angle = asin(ramp_height / ramp_length)

mass = 0.8
g = 10

ballx = 0
ballv = 0

ballx_record = [0]
ballv_record = [0]
balla_record = [g*sin(ramp_angle)]
time_record = [0]

while time_record[-1] < run_time:
    # Force Calculations
    balla = -abs(ballv) * friction_force * mass * g
    if ballx < ramp_length:
        balla += g*sin(ramp_angle)
    
    ballv += balla * delta
    ballx += ballv * delta

    balla_record.append(balla)
    ballv_record.append(ballv)
    ballx_record.append(ballx)
    time_record.append(time_record[-1]+delta)

def ramp_function(x):
    return max(0, tan(ramp_angle)*(ramp_length-x))

fig, axs = plt.subplots(2,2)
fig.suptitle('Rolling Ball')
axs[0,0].plot(time_record, ballx_record)
axs[0,0].set(ylabel="X-position")
axs[1,0].plot(time_record, list(map(ramp_function, ballx_record)))
axs[1,0].set(xlabel="Time", ylabel="Y-position")
axs[0,1].plot(time_record, ballv_record)
axs[0,1].set(ylabel="X-velocity")
axs[1,1].plot(time_record, balla_record)
axs[1,1].set(xlabel="Time", ylabel="X-acceleration")
plt.show()