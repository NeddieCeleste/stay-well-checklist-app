from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QStackedWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QWidget,
)
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QSize, Qt
import sys
from calendar_page import create_calendar_page
from ui.checklist_page import create_checklist_page

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Window settings
    window = QStackedWidget()
    window.setWindowTitle('Stay Well')
    window.setFixedSize(900, 700)
    window.setStyleSheet("background-color: #f2d8e3")
    window.setWindowIcon(QIcon('../graphics/window-icon.png'))

    # Buttons creation
    todo_button = QPushButton('To-do')
    calendar_button = QPushButton('Calendar')
    exit_button = QPushButton('Exit')
    settings_button = QPushButton()


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
    settings_button.setIcon(QIcon('../graphics/settings-button.png'))
    settings_button.setIconSize(QSize(20, 20))
    settings_button.setFixedSize(20, 20)

    todo_button.setStyleSheet(button_style)
    todo_button.clicked.connect(lambda: window.setCurrentIndex(1))
    calendar_button.setStyleSheet(button_style)
    calendar_button.clicked.connect(lambda: window.setCurrentIndex(2))
    exit_button.setStyleSheet(button_style)
    exit_button.clicked.connect(app.quit)



    # Layout settings
    main_layout = QVBoxLayout()
    layout = QHBoxLayout()
    layout.addWidget(todo_button)
    layout.addWidget(calendar_button)
    main_layout.addLayout(layout)



    # Banner settings
    banner = QLabel()
    banner.setFixedHeight(200)
    banner.setStyleSheet("border: 10px groove #d74b88")
    pixmap = QPixmap('../graphics/banner-sample.jpg')
    banner.setPixmap(pixmap)
    banner.setScaledContents(True)
    banner.setAlignment(Qt.AlignmentFlag.AlignCenter)
    banner.setFixedHeight(400)
    banner.setMaximumWidth(900)
    main_layout.addWidget(banner)

    # Side Buttons
    layout.addWidget(settings_button)


    # Bottom Layout
    bottom_layout = QHBoxLayout()
    bottom_layout.addWidget(exit_button)
    main_layout.addLayout(bottom_layout)



    # Pages setup
    checklist_page = create_checklist_page(window)
    calendar_page = create_calendar_page(window)


    main_menu_page = QWidget()
    main_menu_page.setLayout(main_layout)
    window.addWidget(main_menu_page)
    window.addWidget(checklist_page)
    window.addWidget(calendar_page)
    window.show()
    sys.exit(app.exec())