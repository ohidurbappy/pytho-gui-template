#!/bin/bash

# set the icon to a variable
ICON_PATH=assets/icon.png

if [ "$1" == "nuitka" ]; then
    # Build with Nuitka
    python -m nuitka --standalone --follow-imports app.py

elif [ "$1" == "nuitka_macos" ];then

    # Build with Nuitka (onefile)
    python -m nuitka --macos-create-app-bundle --macos-app-icon="$ICON_PATH" app.py
    # python -m nuitka --standalone --show-progress --show-memory --follow-imports --onefile app.py

elif [ "$1" == "nuitka_windows" ]; then

    python -m nuitka --onefile --windows-icon-from-ico="$ICON_PATH" app.py

else
    # Build with PyInstaller (default)
    pyinstaller app.py --name "My App" --onefile --noconsole --icon="$ICON_PATH"
fi

