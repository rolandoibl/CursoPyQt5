import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from TableWidget import DialogIntegrantes

class DialogIntegrantesApplication(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = DialogIntegrantes()
        self.ui.setupUi(self)

        self.InicializarDatos()
        self.AgregarDatos()
        self.show()

    def InicializarDatos(self):
        self.datos = []
        self.datos.append(('Roni','Telecomunicaciones'))
        self.datos.append(('Jorge','Mecatrónica'))
        self.datos.append(('Lis','Computación'))
        self.datos.append(('Brenda','Geológica'))
        self.datos.append(('Rolando','Mecatrónica'))

    def AgregarDatos(self):
        rows = 0
        for registro in self.datos:
            columns = 0
            self.ui.tblIntegrantes.insertRow(rows)
            for elemento in registro:
                cell = QTableWidgetItem(elemento)
                self.ui.tblIntegrantes.setItem(rows,columns,cell)
                columns += 1
            rows += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = DialogIntegrantesApplication()
    ventana.show()
    sys.exit(app.exec_())
