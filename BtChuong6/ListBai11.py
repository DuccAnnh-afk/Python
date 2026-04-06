# Nhập dữ liệu
n = int(input("Nhập n: "))
_list = input("Nhập list (cách nhau bằng dấu cách): ").split()

# Lọc các từ có độ dài > n
result = [x for x in _list if len(x) > n]

print("Các từ thỏa mãn:", result)