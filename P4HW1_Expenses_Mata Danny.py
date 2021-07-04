    # CTI-110
    # P4HW1 - Expenses
    # Danny Mata
    # 04 July 2021

def main():
  amt
amt = float(input("Enter starting amount in account $"))
count = 1
flag = "y"
exp = 0
sum = 0
while flag=="y":
  exp = float(input("Enter expense "+str(count)+": "))
  sum += exp
  flag = input('Do you want to enter another expense? (y/n) ')
  if flag=="y":
    count += 1

total = amt - sum
print("Amount in account before expenses subtracted $"+str(amt))
print("Number of expenses entered: "+str(count))
print("Amount in account after expenses subtracted is $"+str(total))
