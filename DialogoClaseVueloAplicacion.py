import sys
from PyQt5.QtWidgets import QDialog, QApplication
from DialogoClaseVuelo import DialogoClaseVuelo

class DialogoClaseVueloAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.dialogo = DialogoClaseVuelo()
        self.dialogo.setupUi(self)

        self.dialogo.rbtnPrimeraClase.toggled.connect(self.mostrar_informacion)
        self.dialogo.rbtnClaseNegocios.toggled.connect(self.mostrar_informacion)
        self.dialogo.rbtnClaseEconomica.toggled.connect(self.mostrar_informacion)

        self.show()

    def mostrar_informacion(self):
        costo = 0

        if self.dialogo.rbtnPrimeraClase.isChecked() == True:
            costo = 190

        if self.dialogo.rbtnClaseNegocios.isChecked() == True:
            costo = 140

        if self.dialogo.rbtnClaseEconomica.isChecked() == True:
            costo = 100

        self.dialogo.lbResultadoSeleccion.setText("El costo del boleto es de {}".format(costo))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = DialogoClaseVueloAplicacion()
    dialogo.show()
    sys.exit(app.exec_())
