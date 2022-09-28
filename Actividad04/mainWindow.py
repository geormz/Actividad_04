import PySide2
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow


class MainWIndow(QMainWindow):
    def __init__(self):
        super(MainWIndow,self).__init__()
        ui=Ui_MainWindow()
        ui.setupUi(self) ##mete la intrerfaz
        ui.pushButton.clicked.connect(self.click_agregar) ##conectar clase a boton


    @Slot()
    def click_agregar(self):
        print("click")