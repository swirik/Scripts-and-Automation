# 🗂️ Font Installer — Automated Font Installer for Windows (.EXE Included)

A standalone `.exe` tool that automates the downloading, extraction, and installation of fonts on Windows — from `.zip`, `.ttf`, or `.otf` files via direct URLs or a list. No Python installation required. Just **double-click and install** fonts system-wide or per user.

---

## ✅ Features

- ⬇️ Download fonts from direct `.ttf`, `.otf`, or `.zip` URLs  
- 🧠 Skips fonts already installed in `C:\Windows\Fonts`  
- 🗂️ Reads URLs from `font_links.txt` and accepts manual input  
- 🧵 Automatically extracts `.zip` archives  
- 📝 Installs fonts to Windows Fonts folder  
- 🧱 Adds proper registry entries (system or current user)  
- 📊 Real-time download progress via command window  
- 🧾 Summary at the end: installed / skipped / failed  
- 🧹 Optional: delete ZIP files after install  
- 🪵 Errors and actions logged to `install_log.txt`  
- 🔒 Admin and non-admin modes supported  

---

## 🚀 How to Use

### 1. 📁 Download and Extract

Download the `.zip` package and extract it to a folder. You should see:

FontInstaller/

├── FontInstaller.exe # ✅ The one-click executable

├── font_links.txt # 🔗 Your list of font URLs

├── install_log.txt # 📄 Log file (created after run)

└── README.md # 📘 This file

---

### 2. 📝 Add Font URLs

Open `font_links.txt` and paste in one font URL per line, for example:

https://dl.dafont.com/dl/?f=dianora
https://fontsgeek.com/content/font_download/affair-regular.zip

---

### 3. 🖱️ Run the Installer

Just **double-click `FontInstaller.exe`**  
It will:

- Prompt you for:
  - Whether to install fonts **system-wide or current-user only**
  - Whether to delete ZIP files after install
  - An optional manual font URL
- Download and install fonts
- Show a final summary

---

## 📊 Output

Example at the end:

🎉 Summary: 4 installed, 2 skipped, 1 failed.

Check `install_log.txt` for any errors or skipped fonts.

---

## 🔐 Admin Rights

If you choose **system-wide install**, you’ll need to approve a UAC prompt (admin access).

If you choose **current-user**, no admin is needed.

---

## 💡 Notes

- Works on Windows 10 & 11
- Requires **no installation or Python**
- Follows font download redirects (e.g. from dafont.com)
- Already-installed fonts are detected and skipped
- Fonts are copied to `C:\Windows\Fonts` and registered in the Windows registry

---

## 📌 Future Plans

- 🖱️ Drag-and-drop ZIP/TTF/OTF GUI version  
- 📂 Folder-wide font batch install  
- 🧠 Auto-detect font display names from metadata  
- 🐧 Cross-platform support (macOS/Linux paths)  

---

## 👨‍💻 Author

**Created by Swirik**  
For designers, developers, and font hoarders who want fonts — fast.

---
