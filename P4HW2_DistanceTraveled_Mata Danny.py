
# CTI-110
# P4HW2-Distance Traveled
# Danny Mata
# 04 July 2021

again="y"
while again=="y":

    carSpeed = float(input("what is the speed of the car?"))
    timeTraveled = int( input("How many hours has it traveled?"))

    print ( "\nHour","\tDistance Traveled" )
    for currentHour in range (1, timeTraveled + 1 ) :
        distanceTraveled = carSpeed * currentHour
        print ( currentHour,"\t",distanceTraveled)
    print()
    if timeTraveled <= 0:
        print('error ! time entered should be > 0')
        print(carSpeed * 1)
        print("Reenter timeTraveled")
        timeTraveled = int(input("How many hours has it traveled?"))
        print("\nHour", "\tDistance Traveled")
        for currentHour in range(1, timeTraveled + 1):
            distanceTraveled = carSpeed * currentHour
            print(currentHour, "\t", distanceTraveled)

    else:
        print("Speed", carSpeed)
        print("Time", timeTraveled)
        print("Distance traveled", carSpeed * timeTraveled)

    again = input("\nwould you like to enter a different time? (y for yes): ")
