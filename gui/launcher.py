import subprocess

py_file = r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\gui\main.py"

if __name__ == "__main__":
    subprocess.Popen(["python", py_file],
                     creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NO_WINDOW,
                     close_fds=True)
