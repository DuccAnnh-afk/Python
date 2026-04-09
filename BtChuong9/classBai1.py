from datetime import datetime

# a) Tạo class HocVien
class HocVien:
    def __init__(self, ho_ten, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    # b) Hiển thị thông tin
    def show_info(self):
        print("Họ tên:", self.ho_ten)
        print("Email:", self.email)
        print("Điện thoại:", self.dien_thoai)
        print("Địa chỉ:", self.dia_chi)
        print("Lớp:", self.lop)

    # c) Thay đổi thông tin (có mặc định)
    def change_info(self, dia_chi="Hà Nội", lop="IT12.x"):
        self.dia_chi = dia_chi
        self.lop = lop


# d) Chương trình chính
class Main:
    hv1 = HocVien("Nguyen Van A", "a@gmail.com", "090000000", "Ha Nam", "IT14.2")
    hv1.show_info()
    print("--------------")
    hv1.change_info()
    hv1.show_info()
    