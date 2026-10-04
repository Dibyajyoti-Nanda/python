a = list(map(int ,input("Enter elements separating by spaces -: ").split()))
for i in (set(a)):
    print(f"{i} occures {a.count(i)} times")

