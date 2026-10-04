a = int(input("Enter a no to check is it prime or not-: "))
if a <= 0:
    print("It's not a prime  number")

else:
    for i in range(2,a):
        if a % i == 0:
            print("it's not a prime number")
            break
    else:
        print("It's a prime number")