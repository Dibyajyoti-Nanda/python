a = int(input("enter a no you want to print factorial -: "))
factorial = 1
for i in range (1, a+1):
    factorial = factorial*i
    print(f"factorial of {a} is = {factorial}")