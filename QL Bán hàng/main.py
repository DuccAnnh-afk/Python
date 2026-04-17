from controllers import product_controller as pc
from controllers import customer_controller as cc
from controllers import order_controller as oc

def product_menu():
    print("\n1. Xem sản phẩm")
    print("2. Thêm sản phẩm")
    choice = input("Chọn: ")

    if choice == "1":
        for p in pc.get_all_products():
            print(p)

    elif choice == "2":
        name = input("Tên: ")
        origin = input("Nguồn gốc: ")
        price = float(input("Giá: "))
        pc.add_product(name, origin, price)


def customer_menu():
    print("\n1. Xem khách hàng")
    print("2. Thêm khách hàng")
    choice = input("Chọn: ")

    if choice == "1":
        for c in cc.get_all_customers():
            print(c)

    elif choice == "2":
        name = input("Tên: ")
        address = input("Địa chỉ: ")
        phone = input("SĐT: ")
        cc.add_customer(name, address, phone)


def order_menu():
    print("\n1. Tạo đơn hàng")
    print("2. Xem đơn hàng")
    choice = input("Chọn: ")

    if choice == "1":
        cid = int(input("ID khách hàng: "))
        order_id = oc.create_order(cid)

        while True:
            pid = int(input("ID sản phẩm: "))
            qty = int(input("Số lượng: "))
            price = float(input("Giá: "))
            oc.add_order_detail(order_id, pid, qty, price)

            cont = input("Thêm nữa? (y/n): ")
            if cont == "n":
                break

    elif choice == "2":
        for o in oc.get_orders():
            print(o)


def main():
    while True:
        print("\n===== MENU =====")
        print("1. Quản lý sản phẩm")
        print("2. Quản lý khách hàng")
        print("3. Quản lý đơn hàng")
        print("0. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
            product_menu()
        elif choice == "2":
            customer_menu()
        elif choice == "3":
            order_menu()
        elif choice == "0":
            break


if __name__ == "__main__":
    main()