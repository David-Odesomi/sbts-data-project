import os
import shutil
folder = "summary1.txt"
target_folder = r"C:\Users\HP USER\OneDrive\Documents\Desktop\Report"

if os.path.exists(target_folder):
    print("Folder exists")
else:
    os.mkdir(target_folder)

shutil.move(folder, target_folder)
print("Summary 1.txt moved successfully")