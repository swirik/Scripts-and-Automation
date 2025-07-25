import os
import shutil
from pathlib import Path

# Define the Downloads folder (default for most systems)
DOWNLOADS_FOLDER = str(Path.home() / "Downloads")

# Define file categories and extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat", ".sh"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".cs", ".php"],
    "Installers": [".iso", ".img", ".dmg"]
}

def get_category(extension):
    """Return the folder category for the given extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_downloads():
    for filename in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)

        # Skip if it's a folder (including our category folders)
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        if not ext:
            continue  # Skip files with no extension

        category = get_category(ext)
        target_folder = os.path.join(DOWNLOADS_FOLDER, category)

        os.makedirs(target_folder, exist_ok=True)

        destination_path = os.path.join(target_folder, filename)

        # Skip if already exists
        if os.path.exists(destination_path):
            print(f"Skipped (exists): {filename}")
            continue

        shutil.move(file_path, destination_path)
        print(f"Moved: {filename} → {category}/")

if __name__ == "__main__":
    organize_downloads()
