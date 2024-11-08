cd c:\temp

python -m nuitka ^
    --lto=no ^
    --mingw64 ^
    --onefile ^
    --windows-icon-from-ico=image_files_16.ico ^
    --enable-plugin=tk-inter ^
    --windows-console-mode=disable ^
    image_encoder_gui.py
pause