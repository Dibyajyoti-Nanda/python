a = input("enter your first string -: ")
b = input("enter your second string -: ")

a = a.replace(" ","").lower()
b =  b.replace(" ","").lower()

if sorted(a) == sorted(b):
    print("It's anagram")
else:
    print("It's not angram")