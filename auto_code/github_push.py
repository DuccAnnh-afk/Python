import os

def run(cmd):
    print(f"> {cmd}")
    return os.system(cmd)

def push_github():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.abspath(os.path.join(current_dir, ".."))
        os.chdir(root_dir)

        print(" Đang ở:", root_dir)

      
        run("git stash")

       
        run("git pull origin main")

        run("git stash pop")

     
        run("git add .")

        commit_status = run('git commit -m "auto add bai tap"')
        
        run("git push origin main")

        print("✅ Đã push lên GitHub!")

    except Exception as e:
        print("❌ Lỗi:", e)