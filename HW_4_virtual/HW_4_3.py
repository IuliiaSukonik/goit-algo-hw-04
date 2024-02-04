from colorama import Fore, Style, init
import sys
import os
from pathlib import Path
#args = sys.argv
#print(args)
#print(args[0], type(args[0]))

def directory (direct_name):
    name = direct_name[0]
    try:
        directory_name = Path(name)
        dir_path = directory_name.parent
        print(dir_path)
        for new_name in os.listdir(dir_path):
            if os.path.isdir(new_name):
                print(Fore.RED + new_name)

        for n_name in os.listdir(dir_path):
            if os.path.isfile(n_name):
                print(Fore.GREEN + n_name)
                
    except Exception:
        print("ERROR  not correct")

directory(sys.argv)


__name__ == "__main__"