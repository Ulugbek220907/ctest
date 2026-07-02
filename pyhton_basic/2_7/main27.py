import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.number = 0
        pixmap = QPixmap("pyhton_basic/2_7/img.png")
        label2 = QLabel(self)
        label2.setPixmap(pixmap)
        label2.setGeometry(0, 0, pixmap.width(), pixmap.height())
        label2.setScaledContents(True)
        self.label = QLabel("", self)


        self.setWindowTitle("PyQt5 Example")
        self.setGeometry(550, 200, 800, 800)

        self.label.setFont(QFont("Arial", 10))
        self.label.move(350, 300)
        self.label.setStyleSheet("color: black;"
                                 "font-style: bold;")
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.label.setPixmap(pixmap)

        self.button = QPushButton("Click Me", self)
        self.button.move(350, 400)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.number += 1
        self.label.setStyleSheet("color: black;"
                                 "font-style: bold;")
        self.label.setText(f"Count: {self.number}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())






if __name__ == "__main__":
    main()