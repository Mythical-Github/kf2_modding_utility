import subprocess
from pathlib import Path

py_file_dir = Path("scripts/python").resolve()

if __name__ == "__main__":
    subprocess.Popen(["python", str(py_file_dir / "main.py")],
                     creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NO_WINDOW,
                     close_fds=True,
                     cwd=str(py_file_dir))
