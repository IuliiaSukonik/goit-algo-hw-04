from colorama import Fore, Style, init
import sys
import os
from pathlib import Path

def directory (path):
    try:
        dir_path = Path(path)
        for new_name in os.listdir(dir_path):
            if os.path.isdir(new_name):
                print(Fore.RED + new_name)

        for n_name in os.listdir(dir_path):
            if os.path.isfile(n_name):
                print(Fore.GREEN + n_name)
                
    except Exception:
        print("ERROR  not correct")

name = sys.argv[1]
directory(name)

