def isprime(n):
    if n <= 1:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
        return True
    
a  = int (input("enter a number to check prime number -: "))

if isprime(a):
    print("it is a prime number")
else:
    print("It is not a prime number")