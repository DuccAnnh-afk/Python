import os
from github_push import push_github

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ===== Lấy danh sách chương =====
def list_chuong():
    return [
        d for d in os.listdir(ROOT)
        if os.path.isdir(os.path.join(ROOT, d)) and "chuong" in d.lower()
    ]

# ===== Lấy danh sách luyện tập =====
def list_luyentap(chuong):
    path = os.path.join(ROOT, chuong)
    return [
        d for d in os.listdir(path)
        if os.path.isdir(os.path.join(path, d))
    ]

# ===== Lấy danh sách bài =====
def list_bai(chuong, luyentap):
    path = os.path.join(ROOT, chuong, luyentap)
    return [
        f for f in os.listdir(path)
        if f.endswith(".py")
    ]

# ===== MAIN =====
def main():
    # --- Chọn chương ---
    chuongs = list_chuong()

    print("Danh sách chương:")
    for i, ch in enumerate(chuongs, 1):
        print(f"{i}. {ch}")

    choice = int(input("Chọn chương: ")) - 1
    chuong = chuongs[choice]

    # --- Chọn luyện tập ---
    luyentaps = list_luyentap(chuong)

    print(f"\n--- {chuong} ---")
    for i, lt in enumerate(luyentaps, 1):
        print(f"{i}. {lt}")

    choice_lt = int(input("Chọn luyện tập: ")) - 1
    luyentap = luyentaps[choice_lt]

    # --- Chọn bài ---
    bais = list_bai(chuong, luyentap)

    print(f"\n--- {chuong}/{luyentap} ---")
    for i, bai in enumerate(bais, 1):
        print(f"{i}. {bai}")

    select = input("Chọn bài (số hoặc 'all'): ")

    if select.lower() == "all":
        print("Push toàn bộ bài...")
    else:
        bai = bais[int(select) - 1]
        print(f"Push {bai}...")

    # --- Push Git ---
    push_github()

if __name__ == "__main__":
    main()