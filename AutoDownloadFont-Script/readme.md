🗂️ Font Installer — Automated Font Installer for Windows

A Python-based tool that automates the downloading, extraction, and installation of fonts on Windows systems from online URLs or local .zip/.ttf/.otf files. It supports both system-wide and user-level installations, skips duplicates, and includes useful logs and progress feedback.



✅ Features

⬇️ Downloads fonts from direct .ttf, .otf, or .zip URLs



🧠 Skips already-installed fonts to avoid duplicates



🗂️ Reads from font\_links.txt and allows manual URL input



🧵 Extracts font files from .zip archives automatically



📝 Adds fonts to the Windows Fonts folder



🧱 Adds registry entries (user or system)



📊 Shows real-time progress bars for downloads



🧾 Provides a summary of installed/skipped/failed fonts



🧹 Optional post-install cleanup of ZIP files



🪵 Logs errors and actions to install\_log.txt



🔒 Supports both system-wide and current user only installations



📁 Project Structure

bash

Copy

Edit

FontInstaller/

├── install\_fonts.py         # Main Python script

├── install\_fonts.bat        # One-click Windows launcher (admin)

├── font\_links.txt           # List of font download URLs

├── install\_log.txt          # Log file (auto-generated)

└── README.md                # This file

🚀 How to Use

1\. 📦 Install Requirements (once):

Make sure Python is installed, then run:



bash

Copy

Edit

pip install requests tqdm

2\. 📝 Add Font URLs:

Add one or more download links to font\_links.txt. Example:



arduino

Copy

Edit

https://dl.dafont.com/dl/?f=dianora

https://fontsgeek.com/content/font\_download/affair-regular.zip

3\. 🖱️ Run the Installer:

Just double-click install\_fonts.bat. This will:



Run the Python script as Administrator



Prompt you for:



Install level (current user or system-wide)



Whether to delete ZIP files after install



Optionally enter another URL manually



📊 Output

At the end, you’ll see a summary like:



css

Copy

Edit

🎉 Summary: 4 installed, 2 skipped, 1 failed.

All logs are saved to install\_log.txt.



🔐 Admin Rights

To install fonts system-wide, you need admin privileges. The batch file automatically launches the script with UAC prompt using:



bat

Copy

Edit

powershell -Command "Start-Process python -ArgumentList 'install\_fonts.py' -Verb RunAs"

💡 Tips \& Notes

URLs must be direct downloads or links that redirect to .zip, .ttf, or .otf files.



Manual input works for quick one-off installs.



Drag-and-drop or GUI support can be added in the future.



📌 Future Improvements (Optional Ideas)

GUI version (drag-and-drop fonts or paste URLs)



Install fonts from a folder of ZIPs



Auto-detect display names from font metadata



Cross-platform (Linux/macOS compatibility)



👨‍💻 Author / Maintainer

Built by Swirik

Useful for designers, developers, and anyone who installs fonts often.

