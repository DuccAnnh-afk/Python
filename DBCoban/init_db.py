from db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS nhansu (
    cccd TEXT PRIMARY KEY,
    ten TEXT,
    ngaysinh TEXT,
    gioitinh TEXT,
    diachi TEXT
)
""")

conn.commit()
conn.close()

print("Đã tạo database")