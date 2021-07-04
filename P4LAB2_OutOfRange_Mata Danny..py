a = int(input('Enter first integer'))
b = int(input('Enter second integer'))
if a <= b:
    while a <= b:
        print(a, end=" ")
        a = a + 5
else:
    print("Second integer can't be less than the first")
