a = int(input("Enter a number to check the number if it is palindrome or not -: "))
temp = a
rev = 0
while a > 0:
    digit = a % 10
    rev = (rev * 10) + digit
    a//=10
if rev == temp:
    print("It is palindrome ")
else:
    print("It is not plaindrome")