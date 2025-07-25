# 🗂️ Organize Files by Year and Month (with EXIF Support)

An executable that organizes your **photos and videos** into folders based on **year and month** using the file's original date.

- 📸 For images like `.jpg` or `.jpeg`, it uses **EXIF metadata** (date taken)
- 📁 For other files (e.g. `.mp4`), it falls back to the **file creation date**

---

## ✅ Features

- 📅 Organizes files into:  
YourFolder/

├── 2022/

│ └── March/

├── 2023/

│ └── November/

└── 2024/

└── July/


- 🔁 Works **recursively** (includes files from subfolders)
- 📂 Auto-creates destination folders
- 🧠 Skips already-organized folders
- 🔒 Renames duplicates to avoid overwriting
- 🖱️ Drag-and-drop or manual folder input
- ⏸️ Optional pause (`Press Enter to close...`) for `.exe` usability

---

## 📦 Requirements (for Python script)

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) library for EXIF metadata support

## 📥 Install Pillow


pip install pillow

🚀 How to Use
🐍 Python Script

Save the script as organize_by_date.py

Open a terminal or command prompt

Run the script:

python organize_by_date.py
You'll be asked to input the folder path (or drag and drop)

📦 EXE Version (No Python Needed)

📥 Download the .exe file (e.g., organize_by_date.exe)

🖱️ Double-click to run

📂 Drag and drop a folder or type its full path

✅ Done! Your files will be sorted into year/month folders

⏱️ Optional: Automate It

## To have it run automatically:

Windows Task Scheduler:

Schedule the EXE to run on a folder every day or on file change

Or integrate into context menu via .bat or .reg

## 🧾 Notes

🖼 Works best with image formats that support EXIF (e.g., .jpg, .jpeg)

📹 Falls back to file creation date for other formats (like .mp4)

🚫 Does not delete or compress files

📦 Duplicates will be renamed, not overwritten

## 👨‍💻 Author
Created by Swirik