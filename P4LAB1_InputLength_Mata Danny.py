line = input()
counter = 0
for letter in line:
    if letter.isalpha():
        counter = counter + 1
print(counter)
