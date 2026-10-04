a = input('Enter a sentence -: ')

word = a.split()

long = max(word , key = len)

print(f"Longest word in the sentence is {long}")


