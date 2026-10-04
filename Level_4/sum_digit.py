a  = int(input("Enter a no -: "))
sum_of_digit = 0

while a>0:
    digit = a % 10
    sum_of_digit += digit
    a//=10
print(f"The Sum of digits are {sum_of_digit}")

