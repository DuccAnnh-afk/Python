a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
if a + b > c and a + c > b and b + c > a:
    print("Ba cạnh này có thể tạo thành một tam giác.")
else:
    print("Ba cạnh này không thể tạo thành một tam giác.")