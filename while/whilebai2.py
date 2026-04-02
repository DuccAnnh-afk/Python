n = int(input("Nhập n: "))

giai_thua = 1
i = 1

while i <= n:
    giai_thua *= i
    i += 1

print("n! =", giai_thua)