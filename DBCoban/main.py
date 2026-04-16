from nhansu import NhanSu
from nhansu_service import NhanSuService

def menu():
    print("\n===== QUẢN LÝ NHÂN SỰ =====")
    print("1. Thêm")
    print("2. Sửa")
    print("3. Xóa")
    print("4. Hiển thị")
    print("5. Tìm kiếm")
    print("0. Thoát")

service = NhanSuService()

while True:
    menu()
    chon = input("Chọn: ")

    if chon == "1":
        ns = NhanSu(
            input("CCCD: "),
            input("Tên: "),
            input("Ngày sinh: "),
            input("Giới tính: "),
            input("Địa chỉ: ")
        )
        service.them(ns)

    elif chon == "2":
        service.sua(input("Nhập CCCD: "))

    elif chon == "3":
        service.xoa(input("Nhập CCCD: "))

    elif chon == "4":
        service.hien_thi()

    elif chon == "5":
        service.tim_kiem(input("Nhập từ khóa: "))

    elif chon == "0":
        break