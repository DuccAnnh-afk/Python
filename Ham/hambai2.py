def tong_n_so(n):
    tong = 0
    for i in range(n):
        x = int(input(f"Nhap so thu {i+1}: "))
        tong += x
    return tong

n = int(input("Nhap so luong so: "))
print("Tong =", tong_n_so(n))