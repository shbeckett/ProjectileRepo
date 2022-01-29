import math
print("Hi there, you gun-toting psychopath. Would you like to know how high your bullet will be at any point in its trajectory? Of course you would.")
accel = 9.81
vel = float(input("What is the initial velocity in metres per second? "))
theta =float(input("What is the angle of elevation in degrees? " )) * (math.pi/180)
dist = float(input("What is the horizontal distance travelled in metres? "))
barh = float(input("What is the barrel height in metres? "))
projh = barh + dist * math.tan(theta) - (accel*dist**2 / (2*(vel * math.cos(theta))**2))
print("Your bullet is " + str(projh) + "m high.")

#What I learned
#Specifying/casting data type is important with inputs and precedes them eg float(input("What does this cost?"))
#Can't concatenate float and string data - must recast the float data to string to match eg str(projh)
#Adding an extra space within "" after questions looks nicer for inputs
#**2 is a quicker way of squaring a variable than multiplying it by itself  