import math
a = float(input("Enter a -: "))
b = float(input("Enter b -: "))
c = float(input("Enter c -: "))

d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d))/(2*a)
    root2 = (-b - math.sqrt(d))/(2*a)
    print("Roots are real and distinct")
    print(f"root1 : {root1}")
    print(f"root2 : {root2}")

elif d == 0:
    root = -b/(2*a)
    print("roots are real and equal ")
    print(f"root : {root}")

else:
    real = -b / (2*a)
    imag = math.sqrt(-d)/(2*a)
    print(f"root1 = {real} + {imag}i")
    print(f"root2 = {real} - {imag}i")









