import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('مدير الانتخابات')  # Title in Arabic
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel('مرحبًا بكم في برنامج إدارة الانتخابات!', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())