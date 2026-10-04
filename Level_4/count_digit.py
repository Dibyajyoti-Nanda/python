a = int(input("Enter a no -: "))
count = 0

if a == 0:
    count = 1
else:
    while a > 0 :
        count += 1
        a//=10
print(f"The number of digits are {count}")

