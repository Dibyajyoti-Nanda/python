a  = input ("Enter a string -: ")
vowels = 0
consonannt = 0 
for ch in a.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonannt += 1

print(f"The no of vowels is {vowels}")
print(f"the no of consonant is {consonannt}")