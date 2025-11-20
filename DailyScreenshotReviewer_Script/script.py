import os
import shutil
import datetime
import subprocess
import platform

SCREENSHOT_FOLDER = os.path.expanduser("~/Pictures/Screenshots")
today = datetime.datetime.now().strftime("%Y-%m-%d")
dest_folder = os.path.join(SCREENSHOT_FOLDER, f"Review_{today}")

files_today = []
for file in os.listdir(SCREENSHOT_FOLDER):
    full_path = os.path.join(SCREENSHOT_FOLDER, file)
    if os.path.isfile(full_path):
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(full_path)).strftime("%Y-%m-%d")
        if mtime == today:
            files_today.append(full_path)

if len(files_today) == 0:
    exit()

os.makedirs(dest_folder, exist_ok=True)

moved_files = []
for file in files_today:
    new_path = os.path.join(dest_folder, os.path.basename(file))
    shutil.move(file, new_path)
    moved_files.append(new_path)

def open_file(path):
    system = platform.system()
    if system == "Windows":
        os.startfile(path)
    elif system == "Darwin":
        subprocess.run(["open", path])
    else:
        subprocess.run(["xdg-open", path])

for file in moved_files:
    open_file(file)
