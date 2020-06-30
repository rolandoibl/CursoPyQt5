# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditorComidasFav.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ComidasFavoritasVentana(object):
    def setupUi(self, ComidasFavoritasVentana):
        ComidasFavoritasVentana.setObjectName("ComidasFavoritasVentana")
        ComidasFavoritasVentana.resize(451, 321)
        self.lstComidas = QtWidgets.QListWidget(ComidasFavoritasVentana)
        self.lstComidas.setGeometry(QtCore.QRect(10, 80, 431, 192))
        self.lstComidas.setObjectName("lstComidas")
        self.btnEditar = QtWidgets.QPushButton(ComidasFavoritasVentana)
        self.btnEditar.setGeometry(QtCore.QRect(10, 280, 131, 28))
        self.btnEditar.setObjectName("btnEditar")
        self.btnEliminar = QtWidgets.QPushButton(ComidasFavoritasVentana)
        self.btnEliminar.setGeometry(QtCore.QRect(150, 280, 161, 28))
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnEliminarTodos = QtWidgets.QPushButton(ComidasFavoritasVentana)
        self.btnEliminarTodos.setGeometry(QtCore.QRect(320, 280, 121, 28))
        self.btnEliminarTodos.setObjectName("btnEliminarTodos")
        self.lbIngresaComida = QtWidgets.QLabel(ComidasFavoritasVentana)
        self.lbIngresaComida.setGeometry(QtCore.QRect(20, 20, 161, 16))
        self.lbIngresaComida.setObjectName("lbIngresaComida")
        self.ledtComida = QtWidgets.QLineEdit(ComidasFavoritasVentana)
        self.ledtComida.setGeometry(QtCore.QRect(230, 20, 211, 22))
        self.ledtComida.setObjectName("ledtComida")
        self.btnAgregar = QtWidgets.QPushButton(ComidasFavoritasVentana)
        self.btnAgregar.setGeometry(QtCore.QRect(230, 50, 211, 28))
        self.btnAgregar.setObjectName("btnAgregar")

        self.retranslateUi(ComidasFavoritasVentana)
        QtCore.QMetaObject.connectSlotsByName(ComidasFavoritasVentana)

    def retranslateUi(self, ComidasFavoritasVentana):
        _translate = QtCore.QCoreApplication.translate
        ComidasFavoritasVentana.setWindowTitle(_translate("ComidasFavoritasVentana", "Editor de comidas"))
        self.btnEditar.setText(_translate("ComidasFavoritasVentana", "Editar"))
        self.btnEliminar.setText(_translate("ComidasFavoritasVentana", "Eliminar"))
        self.btnEliminarTodos.setText(_translate("ComidasFavoritasVentana", "Eliminar todos"))
        self.lbIngresaComida.setText(_translate("ComidasFavoritasVentana", "Ingresa comida favorita:"))
        self.btnAgregar.setText(_translate("ComidasFavoritasVentana", "Agregar"))

