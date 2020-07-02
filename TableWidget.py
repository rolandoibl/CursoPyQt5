# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TableWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class DialogIntegrantes(object):
    def setupUi(self, DialogIntegrantes):
        DialogIntegrantes.setObjectName("DialogIntegrantes")
        DialogIntegrantes.resize(640, 480)
        self.tblIntegrantes = QtWidgets.QTableWidget(DialogIntegrantes)
        self.tblIntegrantes.setGeometry(QtCore.QRect(50, 30, 511, 341))
        self.tblIntegrantes.setObjectName("tblIntegrantes")
        self.tblIntegrantes.setColumnCount(2)
        self.tblIntegrantes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblIntegrantes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblIntegrantes.setHorizontalHeaderItem(1, item)

        self.retranslateUi(DialogIntegrantes)
        QtCore.QMetaObject.connectSlotsByName(DialogIntegrantes)

    def retranslateUi(self, DialogIntegrantes):
        _translate = QtCore.QCoreApplication.translate
        DialogIntegrantes.setWindowTitle(_translate("DialogIntegrantes", "Integrantes delphia"))
        item = self.tblIntegrantes.horizontalHeaderItem(0)
        item.setText(_translate("DialogIntegrantes", "Nombre"))
        item = self.tblIntegrantes.horizontalHeaderItem(1)
        item.setText(_translate("DialogIntegrantes", "Carrera"))

