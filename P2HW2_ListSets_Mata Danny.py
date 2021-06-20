
# CTI-110
# P2HW2 - List and Sets
# Danny Mata
# 20 June 2021

print("Enter a series of 10 numbers: ")

list = []
i = 0

while i < 10:
    list.append(int(input()))
    i += 1

total = sum(list)

average = total / 10

print("The lowest number in the list is: ", min(list))
print("The highest number in the list is: ", max(list))
print("The total of the numbers in the list is: ", total)
print("The average of the numbers in the list is: ", average)
numbers = list
numbers = set(numbers)
print(numbers)
