from PyQt6.QtWidgets import QApplication, QLabel, QWidget
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Stay Well')
window.setGeometry(300, 300, 900, 600)

label = QLabel('In progress', parent=window)
label.move(200, 200)

window.show()
sys.exit(app.exec())