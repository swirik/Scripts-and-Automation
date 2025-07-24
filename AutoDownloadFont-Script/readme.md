# 🗂️ Font Installer — Automated Font Installer for Windows

A Python-based tool that automates the downloading, extraction, and installation of fonts on Windows systems from `.zip`, `.ttf`, or `.otf` files — either via direct URLs or a list file. It supports both **system-wide** and **current user** installations, skips duplicates, shows real-time progress, and logs activity.

---

## ✅ Features

- ⬇️ Download fonts from direct `.ttf`, `.otf`, or `.zip` URLs
- 🧠 Skips fonts already installed in `C:\Windows\Fonts`
- 🗂️ Reads URLs from `font_links.txt` and accepts manual input
- 🧵 Automatically extracts `.zip` archives
- 📝 Installs fonts to Windows Fonts folder
- 🧱 Adds proper registry entries (system or current user)
- 📊 Real-time download progress with `tqdm`
- 🧾 Summary report at the end (installed / skipped / failed)
- 🧹 Optional cleanup: deletes downloaded ZIPs after install
- 🪵 Logs errors and actions to `install_log.txt`
- 🔒 Works with Admin or non-Admin accounts

---

## 📁 Project Structure

FontInstaller/
├── install_fonts.py # Main Python script
├── install_fonts.bat # One-click Windows launcher (with UAC)
├── font_links.txt # List of font download URLs
├── install_log.txt # Auto-generated error log
└── README.md # Project readme

yaml
Copy
Edit

---

## 🚀 How to Use

### 1. 📦 Install Requirements (first time only)
Make sure Python is installed, then open a terminal and run:

```bash
pip install requests tqdm
2. 📝 Add Font URLs
Edit font_links.txt and paste one URL per line:

text
Copy
Edit
https://dl.dafont.com/dl/?f=dianora
https://fontsgeek.com/content/font_download/affair-regular.zip
You can also enter a URL manually during script execution.

3. 🖱️ Run the Installer
Double-click install_fonts.bat to launch the script with admin privileges.

You'll be prompted for:

Whether to install fonts for the current user or system-wide

Whether to delete ZIP files after installing

An optional manual font URL

📊 Output
At the end of the script, you'll see a summary like:

css
Copy
Edit
🎉 Summary: 4 installed, 2 skipped, 1 failed.
All logs are saved in install_log.txt

🔐 Admin Rights
To install fonts system-wide, you’ll need administrator access.

The included .bat file automatically runs the script using UAC elevation:

bat
Copy
Edit
powershell -Command "Start-Process python -ArgumentList 'install_fonts.py' -Verb RunAs"
If you only want per-user fonts, you can run install_fonts.py normally.

💡 Tips & Notes
Supports both direct .zip and .ttf/.otf font URLs

Handles redirects automatically

If a font already exists in C:\Windows\Fonts, it will be skipped

Supports Windows only (for now)

📌 Planned Features (Future Ideas)
Drag-and-drop GUI with Tkinter or PySimpleGUI

Multi-font ZIP folder support

Cross-platform support (Linux/macOS font paths)

Auto-detect font display names

👨‍💻 Author
Built by Swirik
A tool for designers, developers, and font hoarders who want to save time.
