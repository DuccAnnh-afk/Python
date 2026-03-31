while True:
    n = str(input("Nhập số nguyên n: "))
    if int(n) % 2 == 0:
        print(f"{n} là số chia hết cho 2.")
    elif int(n) % 3 == 0:        
        print(f"{n} là số chia hết cho 3.")
    elif int(n) % 2 == 0 and int(n) % 3 == 0:
        print(f"{n} là số chia hết cho 2 và 3.")
    else:
        print(f"{n} không chia hết cho 2 và 3.")
    cont = input("Bạn có muốn tiếp tục không? (y/n): ")
    if cont.lower() != 'y':
        break


