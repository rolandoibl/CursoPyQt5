# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EventosDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class EventosDialog(object):
    def setupUi(self, EventosDialog):
        EventosDialog.setObjectName("EventosDialog")
        EventosDialog.resize(357, 300)
        self.txtTexto = QtWidgets.QLineEdit(EventosDialog)
        self.txtTexto.setGeometry(QtCore.QRect(60, 30, 211, 22))
        self.txtTexto.setObjectName("txtTexto")
        self.btnCambio = QtWidgets.QPushButton(EventosDialog)
        self.btnCambio.setGeometry(QtCore.QRect(120, 110, 93, 28))
        self.btnCambio.setObjectName("btnCambio")

        self.retranslateUi(EventosDialog)
        self.btnCambio.clicked.connect(self.txtTexto.clear)
        QtCore.QMetaObject.connectSlotsByName(EventosDialog)

    def retranslateUi(self, EventosDialog):
        _translate = QtCore.QCoreApplication.translate
        EventosDialog.setWindowTitle(_translate("EventosDialog", "Señales y slot"))
        self.btnCambio.setText(_translate("EventosDialog", "Clear"))

