a = input("Enter a string -: ")
for ch in set(a):
    print(f"{ch} : {a.count(ch)}")