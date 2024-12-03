cd c:\temp

python -m nuitka ^
    --lto=no ^
    --mingw64 ^
    --onefile ^
    --windows-icon-from-ico=./examples/image_files_16.ico ^
    --enable-plugin=tk-inter ^
    --nofollow-import-to=PySide6 ^
    --windows-console-mode=disable ^
    image_encoder_gui.py
pause