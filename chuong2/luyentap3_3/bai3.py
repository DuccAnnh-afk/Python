import time

now = time.localtime()

print(
    f"Hom nay la ngay {now.tm_mday} thang {now.tm_mon} nam {now.tm_year} "
    f"gio {now.tm_hour} phut {now.tm_min} giay {now.tm_sec}."
)

a = int(input("Nhap nam sinh: "))
b = now.tm_year - a

print(f"Ban da {b} tuoi.")

before_1630 = now.tm_hour < 16 or (now.tm_hour == 16 and now.tm_min < 30)

if 6 <= b < 18 and before_1630:
    print("Lo ma di hoc di, nghich vo van qua!!")
elif b < 18:
    print("Ban la nguoi chua thanh nien.")
elif b < 60:
    print("Ban la nguoi truong thanh.")
else:
    print("Ban la nguoi cao tuoi.")
