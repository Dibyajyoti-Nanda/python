a = int(input("enter a no to check if it's armstrong -: "))

len_digit = len(str(a))

temp = a
armstrong_sum = 0

while a>0:
    digit = a % 10
    armstrong_sum += (digit ** len_digit)
    a//=10

if temp == armstrong_sum:
    print("It's an armstrong number")
else:
    print("It's not an armstrong number")

