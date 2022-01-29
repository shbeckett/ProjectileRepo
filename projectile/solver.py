import math
accel = 9.81
vel = 44
theta = 80*(math.pi/180)
dist = 0.5
barh = 1
projh = barh + dist * math.tan(theta) - (accel*dist**2 / (2*(vel * math.cos(theta))**2))
print(projh)

#What I learned...
#use import math at top then methods take math. prefix
#if you want to print a variable don't use "
