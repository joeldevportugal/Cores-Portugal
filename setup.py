import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["tkinter", "threading", "_threading_local", "customtkinter","tkinter.ttk", "tkinter.font"],
    "include_files": ["C:\\Users\\HP\\Desktop\\projectos\\programas\\selector de cores\\icon.ico"],  # Substitua pelo caminho do seu ícone
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use "Win32GUI" para aplicativos GUI no Windows

setup(
    name="main2",
    version="1.0",
    description="Descrição da sua aplicação",
    options={"build_exe": build_exe_options},
    executables=[Executable("main2.py", base=base)],
)
