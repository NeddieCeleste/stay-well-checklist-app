# Stay Well Checklist App
A calming, pink-themed productivity application built with Python and PyQt6. This app allows users to manage daily checklists and track dates with an integrated calendar.
# Visuals
<img width="896" height="726" alt="image" src="https://github.com/user-attachments/assets/b9816330-fb73-41e7-a686-7556d902a7e7" />
<img width="894" height="725" alt="image" src="https://github.com/user-attachments/assets/03de3415-5811-4bc4-b533-9d2a6b25a0cd" />
<img width="895" height="721" alt="image" src="https://github.com/user-attachments/assets/a0fb17f9-33a9-4c64-a877-be2b7c7b5c91" />

# Installation & Setup

- Prerequisites
  * Python 3.10+
  * PyQt6

- How to Run from Source
  * Clone the repository:
    
```git clone https://github.com/NeddieCeleste/be-well-checklist-app.git```
```cd be-well-checklist-app```

- Install Dependencies
  * pip install PyQt6
  * Run the application: Launch the app from the root directory to ensure all paths load correctly:

```python ui/main_menu_ui.py```

- How to Build the EXE File
  * To package this app for Windows:

    Install PyInstaller: ```pip install pyinstaller```

  * Run the build command:

```pyinstaller --noconsole --onedir -n "Stay Well" --icon="graphics/window-icon.ico" --paths=. --paths=ui ui/main_menu_ui.py```

# Important: After building, copy the graphics/ and data/ folders into the dist folder and make sure icon paths are ```../graphics```..., so the EXE can find the assets.
