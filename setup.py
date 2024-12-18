import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["tkinter", "pandas", "datetime", "locale"],
    "excludes": [],
    "include_files": [],
}

# GUI applications require a different base on Windows
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="WhatsApp Journal Parser",
    version="1.0",
    description="Aplikasi Parser Jurnal WhatsApp",
    options={"build_exe": build_exe_options},
    executables=[Executable("whatsapp_journal_parser.py", base=base, icon="icon.ico")]
)