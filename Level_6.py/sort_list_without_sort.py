a = list(map(int ,input("Enter elements separating by spaces -: ").split()))

for i in range(len(a)):
    for j in range(0 , len(a) - i - 1):
        if a[j] > a[j+1]:
            a[j] , a[j+1] = a[j+1] , a[j]

print(f"sorted list {a}")