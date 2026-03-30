def generate_code(noidung):
    noidung = noidung.lower()

    if "chia hết cho 2" in noidung and "3" in noidung:
        return """n = int(input("Nhập số nguyên dương: "))

if n % 2 == 0 and n % 3 == 0:
    print("Chia hết cho cả 2 và 3")
elif n % 2 == 0:
    print("Chia hết cho 2")
elif n % 3 == 0:
    print("Chia hết cho 3")
else:
    print("Không chia hết cho 2 hoặc 3")
"""

    elif "phương trình bậc 2" in noidung:
        return """import math

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
"""
    else:
        return "# Chưa hỗ trợ"