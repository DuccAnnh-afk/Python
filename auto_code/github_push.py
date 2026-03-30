import os

def push_github():
    try:
        # lấy đường dẫn file hiện tại
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # đi về root (luuthetoan)
        root_dir = os.path.abspath(os.path.join(current_dir, ".."))

        os.chdir(root_dir)

        os.system("git add .")
        os.system('git commit -m "auto add bai tap"')
        os.system("git push")

        print("Đã push lên GitHub!")
    except Exception as e:
        print("Lỗi:", e)