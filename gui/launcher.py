import subprocess

py_file = "main.py"

if __name__ == "__main__":
    subprocess.Popen(["python", py_file],
                     creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NO_WINDOW,
                     close_fds=True)
