import os
import requests
import zipfile
import shutil
import ctypes
from pathlib import Path

FONT_DIR = os.path.join(os.environ['WINDIR'], 'Fonts')
REG_PATH = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts"
FONT_LINKS_FILE = 'font_links.txt'
TEMP_DIR = Path(os.environ['TEMP']) / "FontInstaller"

# Admin check
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Add font to registry
def add_font_to_registry(font_path):
    import winreg
    font_name = font_path.stem + " (TrueType)"
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, font_name, 0, winreg.REG_SZ, font_path.name)
        print(f"✅ Registered: {font_name}")
    except PermissionError:
        print(f"❌ Permission denied when registering: {font_name}")

# Install font files
def install_fonts_from_zip(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(TEMP_DIR / "unzipped")

    for root, _, files in os.walk(TEMP_DIR / "unzipped"):
        for file in files:
            if file.lower().endswith(('.ttf', '.otf')):
                font_file = Path(root) / file
                target_path = Path(FONT_DIR) / file

                if target_path.exists():
                    print(f"⚠️ Font already installed: {file}")
                    continue

                shutil.copy(font_file, target_path)
                add_font_to_registry(target_path)

# Download ZIP
def download_zip(url):
    try:
        print(f"\n⬇️ Downloading: {url}")
        response = requests.get(url, allow_redirects=True, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200 and response.content[:2] == b'PK':
            zip_path = TEMP_DIR / "font.zip"
            with open(zip_path, 'wb') as f:
                f.write(response.content)
            return zip_path
        else:
            print("❌ Invalid or non-ZIP response.")
    except Exception as e:
        print(f"❌ Failed: {e}")
    return None

def main():
    if not is_admin():
        print("❗ Please run this script as Administrator.")
        return

    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    font_urls = []

    # Read from file
    if Path(FONT_LINKS_FILE).exists():
        with open(FONT_LINKS_FILE, 'r') as f:
            font_urls += [line.strip() for line in f if line.strip().startswith("http")]

    # Optional prompt
    manual = input("Enter an additional font URL (or press Enter to skip): ")
    if manual.strip().startswith("http"):
        font_urls.append(manual.strip())

    # Process
    for url in font_urls:
        zip_path = download_zip(url)
        if zip_path:
            install_fonts_from_zip(zip_path)
            shutil.rmtree(TEMP_DIR / "unzipped", ignore_errors=True)

    print("\n🎉 All fonts processed.")
    input("Press any key to exit")

if __name__ == "__main__":
    main()
