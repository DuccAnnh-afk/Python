import os
from github_push import push_github

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def list_chuong():
    return [
        d for d in os.listdir(ROOT)
        if os.path.isdir(os.path.join(ROOT, d)) 
        and "chuong" in d.lower()
    ]
def list_bai(chuong):
    path = os.path.join(ROOT, chuong)
    result = []

    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(".py"):
                full_path = os.path.join(root, f)
                result.append(full_path)

    return result

def main():
    chuongs = list_chuong()

    print("Danh sách chương:")
    for i, ch in enumerate(chuongs, 1):
        print(f"{i}. {ch}")

    choice = int(input("Chọn chương: ")) - 1
    chuong = chuongs[choice]

    path = os.path.join(ROOT, chuong)

    print(f"\n--- {chuong} ---")

    bais = list_bai(chuong)

    if not bais:
        print("Chưa có bài nào trong chương này!")
        return

    for i, bai in enumerate(bais, 1):
        print(f"{i}. {bai}")

    select = input("Chọn bài (số hoặc 'all'): ")

    # Không cần copy nữa, chỉ cần push
    if select.lower() == "all":
        print("Push toàn bộ bài trong chương...")
    else:
        bai = bais[int(select) - 1]
        print(f"Push {bai}...")

    push_github()

if __name__ == "__main__":
    main()