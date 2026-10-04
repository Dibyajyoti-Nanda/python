a = list(map(int , input("enter first list elements separating by spaces -: ").split()))
b = list(map(int , input("enter second list elements separating by spaces -: ").split()))
merged_list = a + b
merged_list.sort()
print("merged list -: ", merged_list)

