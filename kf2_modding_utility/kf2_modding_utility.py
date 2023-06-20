import os
import subprocess

py_file_dir = "scripts\\python"

os.chdir(py_file_dir)

if __name__ == "__main__":
    subprocess.Popen(["python", "main.py"],
                     creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NO_WINDOW,
                     close_fds=True)
