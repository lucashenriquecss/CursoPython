from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import design



class Api(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnbuscar.clicked.connect(self.acao)

    def acao(self):

        re =self.txtbusca.Text()
        print(re)
        #print(re.json())

r










if __name__ == '__main__':
    qt= QApplication(sys.argv)
    novo = Api()
    novo.show()
    qt.exec_()