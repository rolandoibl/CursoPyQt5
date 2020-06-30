import  sys
from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog, QListWidgetItem
from EditorComidasFav import ComidasFavoritasVentana

class EditorComidasFavApplication(QDialog):
    def __init__(self):
        super().__init__()
        self.dialogo = ComidasFavoritasVentana()
        self.dialogo.setupUi(self)

        self.dialogo.btnAgregar.clicked.connect(self.AgregarComida)
        self.dialogo.btnEditar.clicked.connect(self.EditarComida)
        self.dialogo.btnEliminar.clicked.connect(self.EliminarComida)
        self.dialogo.btnEliminarTodos.clicked.connect(self.EliminarTodos)

        self.show()

    def AgregarComida(self):
        comidaNueva = self.dialogo.ledtComida.text()
        self.dialogo.lstComidas.addItem(comidaNueva)
        self.dialogo.ledtComida.setText('')
        self.dialogo.ledtComida.setFocus()

    def EditarComida(self):
        comidaSeleccionada = self.dialogo.lstComidas.currentRow()
        texto, resultado = QInputDialog.getText(self,"Nueva comida","Ingresa el nombre de la comida")

        if resultado and (len(texto)!=0):
            self.dialogo.lstComidas.takeItem(self.dialogo.lstComidas.currentRow())
            self.dialogo.lstComidas.insertItem(comidaSeleccionada,QListWidgetItem(texto))

    def EliminarComida(self):
        self.dialogo.lstComidas.takeItem(self.dialogo.lstComidas.currentRow())

    def EliminarTodos(self):
        self.dialogo.lstComidas.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = EditorComidasFavApplication()
    dialogo.show()
    sys.exit(app.exec_())