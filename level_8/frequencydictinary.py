a = input("Enter your string-: ")

freq = {}

for ch in a:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for a , b in freq.items():
    print(f"{a} : {b}")