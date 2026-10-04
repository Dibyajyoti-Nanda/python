a = list(map(int ,input("Enter elements separating by spaces -: ").split()))
k = int(input("Enter position number you want to rotate-: "))

rotated = a[-k:] + a[:-k]

print(f"rotated list {rotated}")

