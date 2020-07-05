import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction
from EditorTextoMainWindow import EditorTextoMainWindow

class EditorTextoApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = EditorTextoMainWindow()
        self.ui.setupUi(self)

        self.ui.mniAbrir.triggered.connect(self.Abrir)
        self.ui.mniGuardar.triggered.connect(self.Guardar)
        self.ui.mniSalir.triggered.connect(self.Salir)

        self.show()

    def Abrir(self):
        archivo = QFileDialog.getOpenFileName(self,"Abrir archivo","C:\\","Text files (.txt)")

        if archivo[0]:
            with open(archivo[0],'rt') as f:
                datos = f.read()
                self.ui.txtTexto.setText(datos)

    def Guardar(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        archivo, _ = QFileDialog.getSaveFileName(self,'Guardar archivo','C:\\','Text files(.txt)',options=options)

        with open(archivo, 'wt') as f:
            f.write(self.ui.txtTexto.toPlainText())

    def Salir(self):
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = EditorTextoApplication()
    ventana.show()
    sys.exit(app.exec_())


