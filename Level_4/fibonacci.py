a = int(input("Enter how many terms you want to print fibonacci -: "))

n1 = 0 
n2 = 1
count = 0

if a < 0:
    print("Enter a positive integer")
elif a == 0:
    print(f"the fibonacci series is {n1}")
else:
    while count <= a:
        print(n1,end=" ")

        next_num = n1 + n2
        n1 = n2
        n2 = next_num
        count+=1