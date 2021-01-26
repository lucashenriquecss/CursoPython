import requests
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import json


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DeezeApi')
        self.setGeometry(0,0,900,700)
        self.acao()
        self.show()

    def acao(self):

        btn = QPushButton('CLICK',self)
        btn.setGeometry(200,150,100,30)
        btn.clicked.connect(self.response)
        btn.setText('Buscar')
        self.lblresult = QLabel(self)
        self.lblresult.setText('Result:')
        self.lblresult.move(150,300)
        self.lblresult.resize(200,25)


        self.textbox = QLineEdit(self)
        self.textbox.move(20,20)
        self.textbox.resize(280,40)



    def response(self):
        res =self.textbox.text()
        url = "https://deezerdevs-deezer.p.rapidapi.com/search"
        querystring = {"q": f"{res}"}
        headers = {
            'x-rapidapi-key': "b64785e3c9mshb803013c6a28feep1e24b9jsnb1f94847e4cf",
            'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"
        }
        re = requests.request("GET", url, headers=headers, params=querystring)





















App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())

