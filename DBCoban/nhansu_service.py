from db import get_connection

class NhanSuService:

    def them(self, ns):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO nhansu VALUES (?, ?, ?, ?, ?)",
                (ns.cccd, ns.ten, ns.ngay_sinh, ns.gioi_tinh, ns.dia_chi)
            )
            conn.commit()
            print("✅ Thêm thành công!")
        except Exception as e:
            print("❌ Lỗi:", e)
        finally:
            conn.close()

    def hien_thi(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM nhansu")
        rows = cursor.fetchall()

        if not rows:
            print("Danh sách rỗng!")
        else:
            for r in rows:
                print(r)

        conn.close()

    def xoa(self, cccd):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM nhansu WHERE cccd = ?", (cccd,))
        conn.commit()

        print("✅ Xóa thành công!")
        conn.close()

    def sua(self, cccd):
        conn = get_connection()
        cursor = conn.cursor()

        ten = input("Tên mới: ")
        ns = input("Ngày sinh: ")
        gt = input("Giới tính: ")
        dc = input("Địa chỉ: ")

        cursor.execute("""
        UPDATE nhansu
        SET ten=?, ngaysinh=?, gioitinh=?, diachi=?
        WHERE cccd=?
        """, (ten, ns, gt, dc, cccd))

        conn.commit()
        print("✅ Cập nhật thành công!")
        conn.close()

    def tim_kiem(self, keyword):
        conn = get_connection()
        cursor = conn.cursor()

        k = f"%{keyword}%"
        cursor.execute("""
        SELECT * FROM nhansu
        WHERE cccd LIKE ? OR ten LIKE ? OR diachi LIKE ?
        """, (k, k, k))

        rows = cursor.fetchall()

        if not rows:
            print("❌ Không tìm thấy!")
        else:
            for r in rows:
                print(r)

        conn.close()