a = float(input("Enter First number -: "))
b = input("enter operation('+' , '-' , '*' ,'/' ")
c = float(input("Enter your second number -: "))

match b :
    case '+':
        print(f"result : {a+c}")
    case '-':
        print(f"result : {a-c}")
    case '*':
        print(f"result : {a*c}")
    case '/':
       print(f"result : {a/c}") 
