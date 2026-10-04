a = input("Enter a Word -: ")
vowels = []
consonants = []

for ch in a :
    if ch.lower() in "aeiou":
        vowels.append(ch)
    elif ch.isalpha:
        consonants.append(ch)

print(f"Vowels : {vowels}")
print("no of vowels -: ",len(vowels))
print(f"Consonants : {consonants}")
print("No of consonants -: ", len(consonants))
    