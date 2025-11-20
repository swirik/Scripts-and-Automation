import ctypes
import os
import subprocess
import sys
import winreg
import tkinter as tk
from tkinter import filedialog, messagebox

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, __file__, None, 1
    )
    sys.exit()

def pick_icon_file():
    file_path = filedialog.askopenfilename(
        title="Select a .ico file",
        filetypes=[("ICO files", "*.ico")]
    )
    return file_path

def set_default_folder_icon(ico_path):
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Icons"
    try:
        with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
            winreg.SetValueEx(key, "3", 0, winreg.REG_SZ, ico_path)
        return True
    except PermissionError:
        return False

def reset_folder_icon():
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Icons"
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
            winreg.DeleteValue(key, "3")
        return True
    except FileNotFoundError:
        return True  # Already reset
    except PermissionError:
        return False

def restart_explorer():
    subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.Popen("explorer.exe")

def handle_set_icon():
    ico_path = pick_icon_file()
    if not ico_path:
        messagebox.showinfo("Cancelled", "No file selected.")
        return
    if not os.path.isfile(ico_path) or not ico_path.lower().endswith(".ico"):
        messagebox.showerror("Invalid File", "You must select a valid .ico file.")
        return
    success = set_default_folder_icon(ico_path)
    if success:
        restart_explorer()
        messagebox.showinfo("Success", "Folder icon changed successfully.")
    else:
        messagebox.showerror("Error", "Failed to write to registry. Are you running as admin?")

def handle_reset_icon():
    confirm = messagebox.askyesno("Confirm Reset", "Reset to default folder icon?")
    if not confirm:
        return
    success = reset_folder_icon()
    if success:
        restart_explorer()
        messagebox.showinfo("Reset", "Folder icon has been reset to default.")
    else:
        messagebox.showerror("Error", "Failed to reset icon. Are you running as admin?")

def main():
    if not is_admin():
        run_as_admin()

    root = tk.Tk()
    root.title("🗂️ Folder Icon Tool")
    root.geometry("300x140")
    root.resizable(False, False)

    tk.Label(root, text="Change Default Folder Icon", font=("Segoe UI", 12, "bold")).pack(pady=10)

    tk.Button(root, text="📁 Set Icon", width=20, command=handle_set_icon).pack(pady=5)
    tk.Button(root, text="♻️ Reset to Default", width=20, command=handle_reset_icon).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        error_log = traceback.format_exc()
        try:
            from tkinter import messagebox, Tk
            root = Tk()
            root.withdraw()
            messagebox.showerror("Fatal Error", f"An unexpected error occurred:\n\n{error_log}")
        except:
            print("Fatal error:\n", error_log)
        input("Press Enter to exit...")


