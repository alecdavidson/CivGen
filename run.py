# Imports
from multiprocessing import Pool
import subprocess

# Splash Page
def splash():
    subprocess.call(["python", "splash.py"])
    return "splash"


# Gui
def gui():
    subprocess.call(["python", "gui.py"])
    return "gucci"


# Switcher
def switcher(inp):
    subprocess.run(["python", inp])
    return 1


# Execute
if __name__ == "__main__":
    with Pool(2) as p:
        p.map(switcher, ["gui.py", "splash.py"])
