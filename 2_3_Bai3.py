# Bài 3: Làm việc với 3 số nguyên

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

# a) Tổng và tích
print("Tổng =", a + b + c)
print("Tích =", a * b * c)

# b) Hiệu của 2 số bất kỳ (ví dụ a - b)
print("Hiệu a - b =", a - b)

# c) Chia a cho b
if b != 0:
    print("Chia nguyên a // b =", a // b)
    print("Phần dư a % b =", a % b)
    print("Chia chính xác a / b =", a / b)
else:
    print("Không thể chia cho 0")