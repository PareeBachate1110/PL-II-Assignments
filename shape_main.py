import shapes

print("Enter a number between 1-3 to get the area of the corresponding shape:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

opt = int(input("Enter Number: "))

if opt == 1:
    r = float(input("Enter radius: "))
    area = shapes.circle(r)
    print("Area of Circle =", area)

elif opt == 2:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    area = shapes.rect(l, b)
    print("Area of Rectangle =", area)

elif opt == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = shapes.tri(b, h)
    print("Area of Triangle =", area)

else:
    print("Please enter a valid number.")