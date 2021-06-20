# Distance Traveled
    # 19 June 2021
    # CTI-110 P2HW1 - DistanceTraveled
    # Danny Mata

carSpeed = float(input("what is the speed of the car?"))
timeTraveled = int( input("How many hours has it traveled?"))
print()

print ( "\nHour","\tDistance Traveled" )
for currentHour in range (1, timeTraveled + 1 ) :
    distanceTraveled = carSpeed * currentHour
    print ( currentHour,"\t",distanceTraveled)

print("Speed Entered", carSpeed)
print("Time Entered", timeTraveled)
print("Display distance traveled", distanceTraveled)
