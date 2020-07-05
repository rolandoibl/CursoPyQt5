# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditorTextoMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class EditorTextoMainWindow(object):
    def setupUi(self, EditorTextoMainWindow):
        EditorTextoMainWindow.setObjectName("EditorTextoMainWindow")
        EditorTextoMainWindow.resize(661, 454)
        self.centralwidget = QtWidgets.QWidget(EditorTextoMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtTexto = QtWidgets.QTextEdit(self.centralwidget)
        self.txtTexto.setGeometry(QtCore.QRect(10, 20, 641, 381))
        self.txtTexto.setObjectName("txtTexto")
        EditorTextoMainWindow.setCentralWidget(self.centralwidget)
        self.mbrPrincipal = QtWidgets.QMenuBar(EditorTextoMainWindow)
        self.mbrPrincipal.setGeometry(QtCore.QRect(0, 0, 661, 26))
        self.mbrPrincipal.setObjectName("mbrPrincipal")
        self.menuArchivo = QtWidgets.QMenu(self.mbrPrincipal)
        self.menuArchivo.setObjectName("menuArchivo")
        EditorTextoMainWindow.setMenuBar(self.mbrPrincipal)
        self.statusbar = QtWidgets.QStatusBar(EditorTextoMainWindow)
        self.statusbar.setObjectName("statusbar")
        EditorTextoMainWindow.setStatusBar(self.statusbar)
        self.mniAbrir = QtWidgets.QAction(EditorTextoMainWindow)
        self.mniAbrir.setObjectName("mniAbrir")
        self.mniGuardar = QtWidgets.QAction(EditorTextoMainWindow)
        self.mniGuardar.setObjectName("mniGuardar")
        self.mniSalir = QtWidgets.QAction(EditorTextoMainWindow)
        self.mniSalir.setObjectName("mniSalir")
        self.menuArchivo.addAction(self.mniAbrir)
        self.menuArchivo.addAction(self.mniGuardar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.mniSalir)
        self.mbrPrincipal.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(EditorTextoMainWindow)
        QtCore.QMetaObject.connectSlotsByName(EditorTextoMainWindow)

    def retranslateUi(self, EditorTextoMainWindow):
        _translate = QtCore.QCoreApplication.translate
        EditorTextoMainWindow.setWindowTitle(_translate("EditorTextoMainWindow", "Editor Texto"))
        self.menuArchivo.setTitle(_translate("EditorTextoMainWindow", "Archivo"))
        self.mniAbrir.setText(_translate("EditorTextoMainWindow", "Abrir"))
        self.mniAbrir.setShortcut(_translate("EditorTextoMainWindow", "Ctrl+O"))
        self.mniGuardar.setText(_translate("EditorTextoMainWindow", "Guardar"))
        self.mniGuardar.setShortcut(_translate("EditorTextoMainWindow", "Ctrl+S"))
        self.mniSalir.setText(_translate("EditorTextoMainWindow", "Salir"))
        self.mniSalir.setShortcut(_translate("EditorTextoMainWindow", "Ctrl+Q"))

