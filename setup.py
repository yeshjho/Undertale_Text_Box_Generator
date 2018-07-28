from cx_Freeze import setup, Executable
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [], includes = ["sys", "PyQt5", "PIL", "os"], include_files = ["GUI.ui", "Fonts/", "Images/", "Images_Original/", "ImageError.ui", "TextError.ui", "UnknownError.ui"])
import sys
base = 'Win32GUI' if sys.platform=='win32' else None
executables = [
    Executable('main.py', base=base)
]
setup(
    name='Undertale TextBox Generator',
    version = '1.0',
    description = 'A PyQt TextBox Generator',
    options = dict(build_exe = buildOptions),
    executables = executables
)