def add(*number):
    total = 0
    for num in number:
        total += num
    print(total)

a = list(map(int , input("Enter nos to add -: ").split()))
add(*a)