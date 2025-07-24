import os
import shutil
import zipfile
import requests
import logging
import ctypes
from pathlib import Path
from urllib.parse import urlparse
from tqdm import tqdm

# Windows paths
TEMP_DIR = Path(os.environ.get('TEMP', 'C:\\Temp')) / "FontInstaller"
FONT_DIR = Path(os.environ.get('WINDIR', 'C:\\Windows')) / "Fonts"
LOG_FILE = TEMP_DIR / "install_log.txt"
FONT_LINKS_FILE = Path("font_links.txt")
REG_PATH_SYSTEM = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts"
REG_PATH_USER = r"Software\Microsoft\Windows NT\CurrentVersion\Fonts"

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def download_file(url, target_path):
    try:
        with requests.get(url, stream=True, headers={"User-Agent": "Mozilla/5.0"}) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            with open(target_path, 'wb') as f, tqdm(
                desc=f"⬇️ {os.path.basename(target_path)}",
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
            ) as bar:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        bar.update(len(chunk))
        return True
    except Exception as e:
        logging.error(f"Download failed for {url}: {e}")
        print(f"❌ Failed to download: {url}")
        return False

def is_font_file(file_path):
    return file_path.suffix.lower() in [".ttf", ".otf"]

def get_font_registry_path(current_user=False):
    import winreg
    return (winreg.HKEY_CURRENT_USER if current_user else winreg.HKEY_LOCAL_MACHINE), \
           (REG_PATH_USER if current_user else REG_PATH_SYSTEM)

def font_already_registered(font_name, current_user=False):
    import winreg
    hive, path = get_font_registry_path(current_user)
    try:
        with winreg.OpenKey(hive, path, 0, winreg.KEY_READ) as key:
            i = 0
            while True:
                try:
                    _, value_data, _ = winreg.EnumValue(key, i)
                    if font_name in value_data:
                        return True
                    i += 1
                except OSError:
                    break
    except Exception as e:
        logging.error(f"Error checking registry: {e}")
    return False

def register_font(font_path, current_user=False):
    import winreg
    font_name = font_path.stem + " (TrueType)"
    if font_already_registered(font_path.name, current_user):
        print(f"⚠️  Already registered: {font_path.name}")
        return False
    try:
        hive, path = get_font_registry_path(current_user)
        with winreg.OpenKey(hive, path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, font_name, 0, winreg.REG_SZ, font_path.name)
        return True
    except Exception as e:
        logging.error(f"Error writing to registry: {e}")
        return False

def install_font_file(font_file, current_user):
    target_path = FONT_DIR / font_file.name
    if target_path.exists():
        print(f"⚠️  Font already exists: {font_file.name}")
        return "skipped"
    try:
        shutil.copy(font_file, target_path)
        if register_font(target_path, current_user):
            print(f"✅ Installed: {font_file.name}")
            return "installed"
        else:
            return "failed"
    except Exception as e:
        logging.error(f"Error installing font {font_file.name}: {e}")
        return "failed"

def process_zip(zip_path, current_user):
    installed = skipped = failed = 0
    extract_path = TEMP_DIR / "unzipped"
    if extract_path.exists():
        shutil.rmtree(extract_path)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    for root, _, files in os.walk(extract_path):
        for file in files:
            file_path = Path(root) / file
            if is_font_file(file_path):
                result = install_font_file(file_path, current_user)
                if result == "installed":
                    installed += 1
                elif result == "skipped":
                    skipped += 1
                else:
                    failed += 1
    shutil.rmtree(extract_path, ignore_errors=True)
    return installed, skipped, failed

def main():
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    current_user = input("Install fonts for current user only? (y/N): ").lower() == "y"
    delete_zip = input("Delete downloaded ZIP after install? (Y/n): ").lower() != "n"

    font_urls = []
    if FONT_LINKS_FILE.exists():
        with open(FONT_LINKS_FILE, 'r') as f:
            font_urls += [line.strip() for line in f if line.strip().startswith("http")]

    manual_url = input("Enter a font URL to install (or press Enter to skip): ").strip()
    if manual_url.startswith("http"):
        font_urls.append(manual_url)

    total_installed = total_skipped = total_failed = 0

    for url in font_urls:
        print(f"\n➡️  Processing: {url}")
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "downloaded_file"
        target_path = TEMP_DIR / filename

        if download_file(url, target_path):
            if is_font_file(target_path):
                result = install_font_file(target_path, current_user)
                if result == "installed":
                    total_installed += 1
                elif result == "skipped":
                    total_skipped += 1
                else:
                    total_failed += 1
            elif zipfile.is_zipfile(target_path):
                i, s, f = process_zip(target_path, current_user)
                total_installed += i
                total_skipped += s
                total_failed += f
            else:
                print("❌ Not a font or ZIP file. Skipping.")
                logging.warning(f"Unsupported file format: {url}")

            if delete_zip:
                try:
                    target_path.unlink()
                except Exception as e:
                    logging.error(f"Failed to delete ZIP: {e}")

    print(f"\n🎉 Summary: {total_installed} installed, {total_skipped} skipped, {total_failed} failed.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
