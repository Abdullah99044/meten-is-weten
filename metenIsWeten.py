a = int(input("A Schrijf het getaal"))
b = int(input("B schrijf het getaal"))
if a > b:
    max = a
    print("a is het grootste getal:" , max)
elif a < b:
    min = b
    print("a is het kleinste getal:" , min)
else:
    if a == b:
        print("a en b zijn even groot")
