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
    forme_button = QPushButton('For Me')
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
    forme_button.setStyleSheet(button_style)



    # Layout settings
    main_layout = QVBoxLayout()
    layout = QHBoxLayout()
    layout.addWidget(todo_button)
    layout.addWidget(calendar_button)
    layout.addWidget(forme_button)
    main_layout.addLayout(layout)

    # Mini Calendar Reminders
    mini_calendar_layout = QHBoxLayout()
    calendar_label = QLabel()
    calendar = QPixmap('../graphics/calendar-demo.png')
    calendar_label.setPixmap(calendar)
    calendar_label.setScaledContents(True)
    calendar_label.setFixedSize(200, 200)
    mini_calendar_layout.addWidget(calendar_label)
    # Calendar Reminders
    text_reminders = QVBoxLayout()
    reminders_style = """ 
        QLabel {
            border-bottom: 3px solid #d74b88;
            font-size: 20px;
            color: #7e003d;    
            padding-bottom: -40px;
        }
        QLabel:hover {
            color: #b791a3;
        }
    """
    reminder1 = QLabel('Mom\'s Birthday')
    reminder1.setStyleSheet(reminders_style)
    reminder2 = QLabel('Going to the vet')
    reminder2.setStyleSheet(reminders_style)
    reminder3 = QLabel('Maths exam upcoming!')
    reminder3.setStyleSheet(reminders_style)

    text_reminders.addWidget(reminder1)
    text_reminders.addWidget(reminder2)
    text_reminders.addWidget(reminder3)
    mini_calendar_layout.addLayout(text_reminders)
    main_layout.addLayout(mini_calendar_layout)




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
    side_layout = QHBoxLayout()
    layout.addWidget(settings_button)
    main_layout.addLayout(side_layout)

    # Pages setup
    checklist_page = create_checklist_page(window)


    main_menu_page = QWidget()
    main_menu_page.setLayout(main_layout)
    window.addWidget(main_menu_page)
    window.addWidget(checklist_page)
    window.show()
    sys.exit(app.exec())