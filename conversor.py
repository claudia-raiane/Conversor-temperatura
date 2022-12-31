from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_conversor(object):

    def setupUi(self, conversor):
        conversor.setObjectName("conversor")
        conversor.resize(373, 227)
        conversor.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(conversor)
        self.centralwidget.setObjectName("centralwidget")
        self.botao_converter = QtWidgets.QPushButton(self.centralwidget)
        self.botao_converter.setGeometry(QtCore.QRect(50, 170, 75, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/8725593_check_circle_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_converter.setIcon(icon)
        self.botao_converter.setObjectName("botao_converter")
        self.botao_sair = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sair.setGeometry(QtCore.QRect(200, 170, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Downloads/8726574_x_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_sair.setIcon(icon1)
        self.botao_sair.setObjectName("botao_sair")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, -10, 351, 101))
        self.label.setObjectName("label")
        self.entrada_temperatura = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_temperatura.setGeometry(QtCore.QRect(150, 100, 113, 20))
        self.entrada_temperatura.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.entrada_temperatura.setObjectName("entrada_temperatura")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 81, 21))
        self.label_2.setObjectName("label_2")
        conversor.setCentralWidget(self.centralwidget)

        self.retranslateUi(conversor)
        self.botao_sair.clicked.connect(conversor.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(conversor)
        self.botao_converter.clicked.connect(self.converter)

    def converter(self):
        temp= int(self.entrada_temperatura.text())
        temperatura = (temp-32) * 5/9

        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle("Sucesso!")
        msg.setText(f"Resultado: {temperatura} °C")
        msg.exec()

    def retranslateUi(self, conversor):
        _translate = QtCore.QCoreApplication.translate
        conversor.setWindowTitle(_translate("conversor", "conversor F/°C - versão 1.0"))
        self.botao_converter.setText(_translate("conversor", "Converter"))
        self.botao_sair.setText(_translate("conversor", "Sair"))
        self.label.setText(_translate("conversor", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; color:#00aaff;\">Conversor de temperatura Fahrenheit (F) para Celsius (°C)</span></p></body></html>"))
        self.label_2.setText(_translate("conversor", "<html><head/><body><p><span style=\" font-weight:600;\">Temperatura: </span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_conversor()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())