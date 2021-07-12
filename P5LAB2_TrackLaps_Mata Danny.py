def miles_to_laps(user_miles):
    laps = 4 * user_miles
    return (laps)

miles = float(input("enter the miles:"))
if __name__ == '__main__':
    print('laps completed')
    print('{:.2f}'.format(miles_to_laps(miles)))