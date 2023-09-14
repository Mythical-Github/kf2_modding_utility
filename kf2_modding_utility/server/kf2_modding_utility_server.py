import os
import subprocess

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    py_to_run = os.path.join(script_dir, "scripts", "python", "main.py")

    subprocess.Popen(["python", py_to_run])

if __name__ == "__main__":
    main()
