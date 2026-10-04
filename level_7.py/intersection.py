a = set(map(int , input("Enter the element of first set separating by spaces -: ").split()))
b = set(map(int , input("Enter the element of second set separating by spaces -: ").split()))

result = a.intersection(b)

print("intersection set -: ",result)