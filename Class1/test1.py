# หาพื้นที่สี่เหลี่ยมลบวงกลม
import math
x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))
d = float(input("Enter value of d: "))
result = (x*y) - (math.pi * (d/2) ** 2)
print(f"The law's area is {result:.2f} sq.m.")