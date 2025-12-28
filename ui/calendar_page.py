from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QCalendarWidget,
    QPushButton
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

def create_calendar_page(window):
    calendar_page = QWidget()
    calendar_page.setStyleSheet("background-color: #f2d8e3;")

    # Buttons
    back_button = QPushButton()
    back_button.setIcon(QIcon('../graphics/back-button.png'))
    back_button.setIconSize(QSize(20, 20))
    back_button.setFixedSize(20, 20)
    back_button.clicked.connect(lambda: window.setCurrentIndex(0))

    title = QLabel("Calendar")
    # Matching your "Your Checklists" style
    title.setStyleSheet("""
        font-size: 50px;
        font-family: Segoe Script;
        color: #ae1357;
        border-bottom: 5px solid #ae1357;
    """)

    header_layout = QHBoxLayout()
    header_layout.addWidget(back_button)
    header_layout.addSpacing(30)
    header_layout.addWidget(title)
    header_layout.addStretch()

    # Calendar Widget
    calendar = QCalendarWidget()
    calendar.setGridVisible(True)
    calendar.setStyleSheet("""
        QCalendarWidget QToolButton {
            color: black;
            background-color: #ffb3c1;
            border: 1px solid black;
            border-radius: 5px;
        }
        QCalendarWidget QMenu {
            color: black;
            background-color: white;
        }
        QCalendarWidget QSpinBox {
            color: black;
            background-color: white;
        }
        QCalendarWidget QAbstractItemView:enabled {
            color: black; 
            background-color: white; 
            selection-background-color: #ff8fa3; 
            selection-color: black;
        }
    """)

    # Main Layout
    main_layout = QVBoxLayout()
    main_layout.addLayout(header_layout)
    main_layout.addSpacing(30)
    main_layout.addWidget(calendar)

    calendar_page.setLayout(main_layout)

    return calendar_page