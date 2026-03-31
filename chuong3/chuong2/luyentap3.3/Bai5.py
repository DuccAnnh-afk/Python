import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

delta = b*b - 4*a*c

if delta < 0:
    print("Vô nghiệm")
elif delta == 0:
    print("Nghiệm kép:", -b/(2*a))
else:
    x1 = (-b + delta**0.5)/(2*a)
    x2 = (-b - delta**0.5)/(2*a)
    print("Hai nghiệm:", x1, x2)
