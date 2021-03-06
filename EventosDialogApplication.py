import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication, QWidget
from EventosDialog import EventosDialog

class EventosDialogApplication(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = EventosDialog()
        self.ui.setupUi(self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = EventosDialogApplication()
    dialogo.show()

    sys.exit(app.exec_())
