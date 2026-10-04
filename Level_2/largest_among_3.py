a = int(input("enter first no -: "))
b = int(input("enter second no - : "))
c = int(input("enter your third no - : "))
if a > b > c:
    largest = a
elif b > c:
    largest = b
else:
    largest = c
print(f"largest no among 3 is {largest}")