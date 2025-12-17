from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QPushButton, QScrollArea,
)
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QSize, Qt
from maincode.checklist_functionality import load_tasks
import sys


app = QApplication(sys.argv)

def create_checklist_page(window):
    # Window settings
    loaded_lists = load_tasks()
    checklist_page = QWidget()
    checklist_page.setWindowTitle('Stay Well')
    checklist_page.setFixedSize(900, 700)
    checklist_page.setStyleSheet("background-color: #f2d8e3")
    checklist_page.setWindowIcon(QIcon('../graphics/window-icon.png'))


    # Button settings
    back_button = QPushButton()


    # Button styling
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
    checklist_layout = QVBoxLayout(scroll_area_parent)



    # Checklist boxes:
    for loaded_list in loaded_lists:
        checklist = QFrame()
        checklist.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.5);
            border-radius: 10px;
        """)
        checklist.setFixedSize(700, 200)

        # Name of checklist
        checklist_name = QLabel(loaded_list["Name"])
        checklist_name.setStyleSheet("font-size: 20px; color: black;")

        # Adding the checklist options
        checklist_box_layout = QHBoxLayout(checklist)
        checklist_box_layout.addWidget(checklist_name)
        checklist_box_layout.addStretch()
        delete_checklist_button = QPushButton()
        delete_checklist_button.setIcon(QIcon('../graphics/trash-button.png'))
        delete_checklist_button.setIconSize(QSize(20, 20))
        delete_checklist_button.setFixedSize(20, 20)
        options_button = QPushButton()
        options_button.setIcon(QIcon('../graphics/three-dots.png'))
        options_button.setIconSize(QSize(20, 20))
        options_button.setFixedSize(20, 20)
        checklist_box_layout.addWidget(delete_checklist_button)
        checklist_box_layout.addWidget(options_button)
        checklist_box_layout.setAlignment(Qt.AlignmentFlag.AlignTop)


        checklist_layout.addWidget(checklist)
        checklist_layout.addSpacing(10)

    # Scroll area
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)

    # Closing scroll area
    scroll_area.setWidget(scroll_area_parent)

    # Main layout
    main_layout = QVBoxLayout()
    layout = QHBoxLayout()
    layout.addWidget(back_button)
    layout.addSpacing(30)
    layout.addWidget(functionality_name)
    main_layout.addLayout(layout)
    main_layout.addSpacing(30)
    main_layout.addWidget(scroll_area)


    checklist_page.setLayout(main_layout)
    return checklist_page
