import youtube_dl
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


def funcao3():
    vl = [le.text()]
    with youtube_dl.YoutubeDL() as yl:
        yl.download(vl)

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(400, 200)
janela.setWindowTitle("CruTube")

btn3 = QPushButton("BAIXAR",janela)
btn3.setGeometry(300, 100, 80, 40)
btn3.setStyleSheet('background-color:white; color:red')#background
btn3.clicked.connect(funcao3)

label = QLabel("CRUTUBE",janela)
label.move(10, 10)
label.setStyleSheet('font-size:30px')

label2 = QLabel("LINK :",janela)
label2.move(10, 100)
label2.setStyleSheet('font-size:30px')

le = QLineEdit("",janela)
le.setGeometry(100, 100 , 200, 40)

janela.show()

app.exec()