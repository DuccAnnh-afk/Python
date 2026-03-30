from parser import parse_bai
from generator import generate_code
from github_push import push_github
import os

def save_file(path, so_bai, code):
    filename = os.path.join(path, f"Bai{so_bai}.py")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Đã tạo {filename}")

# ===== CONFIG =====
# 👉 chỉnh đường dẫn mặc định tại đây
DEFAULT_PATH = "../chuong3/luyentap1"

# tạo thư mục nếu chưa có
os.makedirs(DEFAULT_PATH, exist_ok=True)

print("Nhập đề bài (Enter 2 lần để kết thúc):")

text = ""
while True:
    line = input()
    if line == "":
        break
    text += line + "\n"

ds_bai = parse_bai(text)

for so, nd in ds_bai:
    code = generate_code(nd)
    save_file(DEFAULT_PATH, so, code)

# push github
push_github()

print("Hoàn tất!")