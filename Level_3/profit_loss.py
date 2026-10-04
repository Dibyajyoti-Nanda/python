cp = int(input("emter your cost price -: "))
sp = int(input("enter your selling price -: "))

if sp>cp:
    print(f"profit : {sp-cp}")
elif cp>sp:
    print(f"loss : {cp-sp}")
else:
    print("no profit no loss ")