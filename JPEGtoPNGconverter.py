import sys
import os
from PIL import Image

# grab first and second args
starting_loc = sys.argv[1]
final_loc = sys.argv[2]

print(starting_loc)

# check if new exists if not create new
if not os.path.exists(final_loc):
    os.mkdir(final_loc)

# loooooop through pokedex and convert files and place it in new
for root, dirs, all_files in os.walk(starting_loc):
    for files in all_files:
        path = f"{starting_loc}/{files}"
        img = Image.open(path)
        files = f"changed_{files}"
        new_path = files.replace("jpg", 'png')
        new_dir_path = f'{final_loc}/{new_path}'
        img.save(new_dir_path)

