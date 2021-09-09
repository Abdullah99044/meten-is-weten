a = int(input("A Schrijf het getaal"))
max = a
b = int(input("B schrijf het getaal"))
min = b
if a > b:
    max = a
    print("a is het grootste getal:" , max)
elif a < b:
    min = b
    print("a is het kleinste getal:" , min)
else:
    if a == b:
        print("a en b zijn even groot")

print(".............")
print("Het minimum is:" , min)
print("Het maximum is:" , max)
print(".............")
