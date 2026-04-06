# Nhập dữ liệu
n = int(input("Nhập độ dài tối thiểu: "))
_list = input("Nhập list (cách nhau bằng dấu cách): ").split()

count = 0

for x in _list:
    if len(x) >= n and x[0] == x[-1]:
        count += 1

print("Số chuỗi thỏa mãn:", count)