
from PySide6.QtWidgets import QMaiWindow, QApplication, QMessageBox, QFileDialog
from ui_main import Ui_MainWindow
import sys



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Requisição de Compra")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_clar