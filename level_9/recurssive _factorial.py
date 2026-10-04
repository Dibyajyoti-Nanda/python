def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)#recursive call
    
a = int(input("Enter n to print factorial"))
print(fact(a))