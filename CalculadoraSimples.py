# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalculadoraSimples.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(290, 438)
        self.pushButton_13 = QtWidgets.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(220, 300, 61, 61))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_16 = QtWidgets.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(150, 300, 61, 61))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 230, 61, 61))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 160, 61, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std R")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 160, 61, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(150, 230, 61, 61))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 160, 61, 61))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(80, 230, 61, 61))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_17 = QtWidgets.QPushButton(Dialog)
        self.pushButton_17.setGeometry(QtCore.QRect(220, 370, 61, 61))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 61, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 90, 61, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(80, 300, 61, 61))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(10, 300, 61, 61))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(220, 230, 61, 61))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 90, 61, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_19 = QtWidgets.QPushButton(Dialog)
        self.pushButton_19.setGeometry(QtCore.QRect(150, 370, 61, 61))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(80, 160, 61, 61))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 90, 61, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_18 = QtWidgets.QPushButton(Dialog)
        self.pushButton_18.setGeometry(QtCore.QRect(10, 370, 131, 61))
        self.pushButton_18.setObjectName("pushButton_18")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_13.setText(_translate("Dialog", "+"))
        self.pushButton_16.setText(_translate("Dialog", "3"))
        self.pushButton_9.setText(_translate("Dialog", "4"))
        self.pushButton_6.setText(_translate("Dialog", "*"))
        self.pushButton_5.setText(_translate("Dialog", "7"))
        self.pushButton_12.setText(_translate("Dialog", "6"))
        self.pushButton_8.setText(_translate("Dialog", "9"))
        self.pushButton_11.setText(_translate("Dialog", "5"))
        self.pushButton_17.setText(_translate("Dialog", "="))
        self.pushButton.setText(_translate("Dialog", "C"))
        self.pushButton_4.setText(_translate("Dialog", "÷"))
        self.pushButton_14.setText(_translate("Dialog", "2"))
        self.pushButton_15.setText(_translate("Dialog", "1"))
        self.pushButton_10.setText(_translate("Dialog", "-"))
        self.pushButton_3.setText(_translate("Dialog", "√"))
        self.pushButton_19.setText(_translate("Dialog", ","))
        self.pushButton_7.setText(_translate("Dialog", "8"))
        self.pushButton_2.setText(_translate("Dialog", "DEL"))
        self.pushButton_18.setText(_translate("Dialog", "0"))
