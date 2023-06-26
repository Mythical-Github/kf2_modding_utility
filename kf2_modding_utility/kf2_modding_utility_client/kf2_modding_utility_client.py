import os
import sys
import time

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    os.system("python scripts/python/main.py")
    sys.exit()
    
if __name__ == "__main__":
    main()
