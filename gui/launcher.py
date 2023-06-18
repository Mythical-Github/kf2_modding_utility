import subprocess

if __name__ == "__main__":
    subprocess.Popen(["python", r"C:\Users\Mythical\Documents\GitHub\kf2_mythical\gui\main.py"],
                     creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NO_WINDOW,
                     close_fds=True)
