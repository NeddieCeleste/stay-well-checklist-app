from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QPushButton,
    QScrollArea,
    QCheckBox,
    QDialog, QLineEdit,
)
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QSize, Qt
from maincode.checklist_functionality import load_tasks, save_changes
import sys


app = QApplication(sys.argv)


def open_new_checklist_creation():
    # Pop-up window settings
    new_checklist_window = QDialog()
    new_checklist_window.setWindowTitle("New Checklist")
    new_checklist_window.setStyleSheet("background-color: #f2d8e3")
    new_checklist_window.setWindowIcon(QIcon(QPixmap("../graphics/note-popup-icon.png")))
    new_checklist_window.setMinimumSize(400, 600)
    entry_layout = QVBoxLayout()
    entry_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    def add_entry_row():
        new_entry_row = QLineEdit()
        new_entry_row.setStyleSheet("color: black")
        entry_layout.addWidget(new_entry_row)

    # Buttons
    add_entry_button = QPushButton()
    save_checklist_button = QPushButton("Save")
    cancel_button = QPushButton("Cancel")

    # Button Settings:
    add_entry_button.setIcon(QIcon(QPixmap("../graphics/add-entry-button.png")))
    add_entry_button.setIconSize(QSize(30, 30))
    add_entry_button.setFixedSize(30, 30)
    add_entry_button.clicked.connect(add_entry_row)
    button_style = """
                QPushButton {
                    background-color: #d74b88;
                    color: white;
                    border: 2px solid white;
                    padding: 10px;
                    font-size: 20px;
                }
                QPushButton:hover {background-color: #ae1357;}
                QPushButton:pressed {background-color: #b791a3;}
            """
    save_checklist_button.setStyleSheet(button_style)
    cancel_button.setStyleSheet(button_style)
    cancel_button.clicked.connect(new_checklist_window.close)

    # Elements
    name_entry = QLineEdit("Checklist Name: ")
    name_entry.setStyleSheet("color: black; font-size: 20px")

    # Layouts
    main_popup_layout = QVBoxLayout()
    top_layout = QHBoxLayout()
    top_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
    top_layout.addWidget(name_entry)
    top_layout.addWidget(add_entry_button)
    bottom_layout = QHBoxLayout()
    bottom_layout.addWidget(save_checklist_button)
    bottom_layout.addWidget(cancel_button)
    main_popup_layout.addLayout(top_layout)
    main_popup_layout.addLayout(entry_layout)
    main_popup_layout.addLayout(bottom_layout)
    new_checklist_window.setLayout(main_popup_layout)
    new_checklist_window.exec()

def create_checklist_page(window):
    # Window settings
    main_list = load_tasks()
    checklist_page = QWidget()
    checklist_page.setWindowTitle('Stay Well')
    checklist_page.setFixedSize(900, 700)
    checklist_page.setStyleSheet("background-color: #f2d8e3")
    checklist_page.setWindowIcon(QIcon('../graphics/window-icon.png'))


    # Button settings
    back_button = QPushButton()
    add_button = QPushButton('Add Checklist')
    save_button = QPushButton('Save')
    exit_button = QPushButton('Exit')


    # Button styling
    button_style = """
            QPushButton {
                background-color: #d74b88;
                color: white;
                border: 2px solid white;
                padding: 10px;
                font-size: 20px;
            }
            QPushButton:hover {background-color: #ae1357;}
            QPushButton:pressed {background-color: #b791a3;}
        """
    save_button.setStyleSheet(button_style)
    save_button.clicked.connect(lambda: save_changes(main_list))
    exit_button.setStyleSheet(button_style)
    exit_button.clicked.connect(app.quit)
    add_button.setStyleSheet(button_style)
    add_button.clicked.connect(open_new_checklist_creation)
    back_button.setIcon(QIcon('../graphics/back-button.png'))
    back_button.setIconSize(QSize(20, 20))
    back_button.setFixedSize(20, 20)
    back_button.clicked.connect(lambda: window.setCurrentIndex(0))


    # Label settings
    functionality_name = QLabel("Your Checklists")

    # Label style
    functionality_name.setStyleSheet( """
        font-size: 50px;
        font-family: Segoe Script;
        color: #ae1357;
        border-bottom: 5px solid #ae1357;

    """)

    # Checklists layout
    scroll_area_parent = QWidget()
    checklist_scroll_layout = QVBoxLayout(scroll_area_parent)



    # Checklist boxes:
    for loaded_list in main_list:
        checklist = QFrame()
        checklist.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.5);
            border-radius: 10px;
        """)
        checklist.setFixedSize(700, 200)

        # Checklist frame main_layout
        checklist_frame_layout = QVBoxLayout(checklist)

        # Name of checklist
        checklist_name = QLabel(loaded_list["Name"])
        checklist_name.setStyleSheet("font-size: 20px; color: black;")
        checklist_contents = loaded_list["Checklist"]



        # Adding the checklist options

        # Checklist top bar
        checklist_top_bar = QHBoxLayout()
        checklist_top_bar.addWidget(checklist_name)
        checklist_top_bar.addStretch()
        delete_checklist_button = QPushButton()
        delete_checklist_button.setIcon(QIcon('../graphics/trash-button.png'))
        delete_checklist_button.setIconSize(QSize(20, 20))
        delete_checklist_button.setFixedSize(20, 20)
        options_button = QPushButton()
        options_button.setIcon(QIcon('../graphics/three-dots.png'))
        options_button.setIconSize(QSize(20, 20))
        options_button.setFixedSize(20, 20)
        checklist_top_bar.addWidget(delete_checklist_button)
        checklist_top_bar.addWidget(options_button)
        checklist_top_bar.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Checklist bottom bar
        checklist_contents_space = QVBoxLayout()
        for entry_name, is_checked in checklist_contents.items():
            checklist_entry = QCheckBox(entry_name)
            checklist_entry.setChecked(is_checked)
            checklist_entry.setStyleSheet("font-size: 10px; color: black;")
            checklist_entry.toggled.connect(lambda checked, name=entry_name, target_list=loaded_list["Checklist"]: target_list.update({name: checked}))
            checklist_contents_space.addWidget(checklist_entry)

        checklist_frame_layout.addLayout(checklist_top_bar)
        checklist_frame_layout.addLayout(checklist_contents_space)
        checklist_scroll_layout.addWidget(checklist)
        checklist_scroll_layout.addSpacing(10)

    # Scroll area
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)

    # Closing scroll area
    scroll_area.setWidget(scroll_area_parent)

    # Main layout
    main_layout = QVBoxLayout()
    top_page_layout = QHBoxLayout()
    top_page_layout.addWidget(back_button)
    top_page_layout.addSpacing(30)
    top_page_layout.addWidget(functionality_name)
    main_layout.addLayout(top_page_layout)
    main_layout.addSpacing(30)
    main_layout.addWidget(scroll_area)
    bottom_page_layout = QHBoxLayout()
    bottom_page_layout.addWidget(add_button)
    bottom_page_layout.addWidget(save_button)
    bottom_page_layout.addWidget(exit_button)
    main_layout.addLayout(bottom_page_layout)


    checklist_page.setLayout(main_layout)
    return checklist_page
