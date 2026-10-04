a  = float(input("Enter your line input -: "))
if a <= 100:
    bill = a*1.5
elif a<= 200:
    bill = (100*1.5) + (a-100) * 2.5
else:
    bill = (100*1.5)+(100*2.5) + (a - 200)*4
print(f"Electric bill : {bill}")