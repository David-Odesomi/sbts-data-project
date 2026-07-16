import shutil
import os

dir = "/Users/david/Desktop/water"
target = "/Users/david/Desktop/Report"
file = "/Users/david/Desktop/sbts-data-project/output/Summary.txt"

if os.path.exists(dir):
    print("Directory already exists")
else:
    os.mkdir(dir)

shutil.move(file, target)