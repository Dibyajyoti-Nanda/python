a = int(input("Enter a limit you want to print prime no-: "))

for num in range(2,a+1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(f"prime nos are ",num )