from pathlib import Path
import os 

directory_path = Path("/Users/sukonikiuliia/Documents/learning/HW_4_virtual")


for item in directory_path.iterdir():
    print(item.name)

names = [name for name in os.listdir("/Users/sukonikiuliia/Documents/learning/HW_4_virtual")\
         if os.path.isfile(os.path.join("/Users/sukonikiuliia/Documents/learning/HW_4_virtual", name))]

print(names)

dirnames = [name for name in os.listdir("/Users/sukonikiuliia/Documents/learning/HW_4_virtual")
            if os.path.isdir(os.path.join("/Users/sukonikiuliia/Documents/learning/HW_4_virtual", name))]
print(dirnames)