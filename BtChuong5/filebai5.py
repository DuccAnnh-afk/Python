from collections import Counter

with open("demo_file2.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Tách từ
words = text.split()

# Đếm
count = Counter(words)

# In kết quả
print(dict(count))