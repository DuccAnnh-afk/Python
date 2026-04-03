# Nhập thông tin
ten = input("Tên: ")
tuoi = input("Tuổi: ")
email = input("Email: ")
skype = input("Skype: ")
dia_chi = input("Địa chỉ: ")
noi_lam_viec = input("Nơi làm việc: ")

# Lưu file
with open("setInfo.txt", "w", encoding="utf-8") as f:
    f.write(f"Tên: {ten}\n")
    f.write(f"Tuổi: {tuoi}\n")
    f.write(f"Email: {email}\n")
    f.write(f"Skype: {skype}\n")
    f.write(f"Địa chỉ: {dia_chi}\n")
    f.write(f"Nơi làm việc: {noi_lam_viec}\n")

# Đọc lại
print("\nThông tin đã lưu:")
with open("setInfo.txt", "r", encoding="utf-8") as f:
    print(f.read())