text = input("Nhập nội dung: ")

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Đọc lại
with open("output.txt", "r", encoding="utf-8") as f:
    print("Nội dung file:")
    print(f.read())