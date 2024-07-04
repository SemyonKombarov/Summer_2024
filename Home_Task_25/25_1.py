from PyQt6.QtCore import QSize,Qt
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton, QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.setWindowTitle("Home_Task_25_1")
        self.button = QPushButton(f'Количество нажатий на кнопку {self.count}')
        self.button.setFixedSize(400,100)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print(f"Clicked!{self.count+1}")
        # self.button.setText("Other")
        self.count = self.count + 1
        self.button.setText(f'Количество нажатий на кнопку {self.count}')



app = QApplication([])
window = MainWindow()
window.show()
app.exec()
