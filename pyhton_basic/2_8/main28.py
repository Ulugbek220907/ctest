import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QTextEdit, QComboBox, QCheckBox, QRadioButton, QSlider, QProgressBar, QTabWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #window title and size
        self.setWindowTitle("Application")
        self.setGeometry(550, 200, 800, 800)

        #everything else is in the initUI function
        self.initUI()

    def initUI(self):
        #label
        label2 = QLabel("This is a PyQt5 application", self)
        label2.adjustSize()

        #button
        button1 = QPushButton("Click Me", self)
        button1.move(350, 400)
        button1.clicked.connect(self.on_button_click)
    
    def on_button_click(self):
        #action when button is clicked
        print("Button clicked!")







def main():
    #launching the application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

#setting the main function to run when the script is executed
if __name__ == "__main__":
    main()