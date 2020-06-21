import sys
from PyQt5.QtWidgets import QDialog, QApplication
from DialogoSaludo import *

class DialogoSaludoAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.dialogo = Ui_dialogoSaludar()
        self.dialogo.setupUi(self)

        self.dialogo.btnSaludar.clicked.connect(self.mostrar_saludo)
        self.show()

    def mostrar_saludo(self):
        mensaje = self.dialogo.txtNombre.text()
        self.dialogo.lbMensajeSaludo.setText(mensaje)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = DialogoSaludoAplicacion()
    dialogo.show()
    sys.exit(app.exec_())