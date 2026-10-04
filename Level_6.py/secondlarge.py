a = list(map(int,input("Enter element separating spaces -: ").split()))
largest = max(a)
a.remove(largest)
second_largest = max(a)

print(f"second largest element is {second_largest}")


