# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DialogoClaseVuelo.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class DialogoClaseVuelo(object):
    def setupUi(self, DialogoClaseVuelo):
        DialogoClaseVuelo.setObjectName("DialogoClaseVuelo")
        DialogoClaseVuelo.resize(320, 240)
        self.lbEscojaClaseVuelo = QtWidgets.QLabel(DialogoClaseVuelo)
        self.lbEscojaClaseVuelo.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.lbEscojaClaseVuelo.setObjectName("lbEscojaClaseVuelo")
        self.rbtnPrimeraClase = QtWidgets.QRadioButton(DialogoClaseVuelo)
        self.rbtnPrimeraClase.setGeometry(QtCore.QRect(20, 50, 111, 20))
        self.rbtnPrimeraClase.setObjectName("rbtnPrimeraClase")
        self.rbtnClaseNegocios = QtWidgets.QRadioButton(DialogoClaseVuelo)
        self.rbtnClaseNegocios.setGeometry(QtCore.QRect(20, 70, 121, 20))
        self.rbtnClaseNegocios.setObjectName("rbtnClaseNegocios")
        self.rbtnClaseEconomica = QtWidgets.QRadioButton(DialogoClaseVuelo)
        self.rbtnClaseEconomica.setGeometry(QtCore.QRect(20, 90, 131, 20))
        self.rbtnClaseEconomica.setObjectName("rbtnClaseEconomica")
        self.lbResultadoSeleccion = QtWidgets.QLabel(DialogoClaseVuelo)
        self.lbResultadoSeleccion.setGeometry(QtCore.QRect(30, 140, 261, 31))
        self.lbResultadoSeleccion.setText("")
        self.lbResultadoSeleccion.setObjectName("lbResultadoSeleccion")

        self.retranslateUi(DialogoClaseVuelo)
        QtCore.QMetaObject.connectSlotsByName(DialogoClaseVuelo)

    def retranslateUi(self, DialogoClaseVuelo):
        _translate = QtCore.QCoreApplication.translate
        DialogoClaseVuelo.setWindowTitle(_translate("DialogoClaseVuelo", "Clase Vuelo"))
        self.lbEscojaClaseVuelo.setText(_translate("DialogoClaseVuelo", "Escoja la clase de vuelo:"))
        self.rbtnPrimeraClase.setText(_translate("DialogoClaseVuelo", "Primera Clase"))
        self.rbtnClaseNegocios.setText(_translate("DialogoClaseVuelo", "Clase Negocios"))
        self.rbtnClaseEconomica.setText(_translate("DialogoClaseVuelo", "Clase Econ├│mica"))
