a = list(map(int , input("enter first list elements separating by spaces -: ").split()))
b = list(map(int , input("enter second list elements separating by spaces -: ").split()))

common = []

for i in a:
    if i in b:
        common.append(i)

print(f"common items are {common}")
