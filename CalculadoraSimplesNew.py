# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\CalculadoraSimples.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(290, 438)
        self.button_add = QtWidgets.QPushButton(Dialog)
        self.button_add.setGeometry(QtCore.QRect(220, 300, 61, 61))
        self.button_add.setObjectName("button_add")
        self.button_3 = QtWidgets.QPushButton(Dialog)
        self.button_3.setGeometry(QtCore.QRect(150, 300, 61, 61))
        self.button_3.setObjectName("button_3")
        self.button_4 = QtWidgets.QPushButton(Dialog)
        self.button_4.setGeometry(QtCore.QRect(10, 230, 61, 61))
        self.button_4.setObjectName("button_4")
        self.button_multiple = QtWidgets.QPushButton(Dialog)
        self.button_multiple.setGeometry(QtCore.QRect(220, 160, 61, 61))
        self.button_multiple.setObjectName("button_multiple")
        self.label_display = QtWidgets.QLabel(Dialog)
        self.label_display.setGeometry(QtCore.QRect(10, 10, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std R")
        font.setPointSize(36)
        self.label_display.setFont(font)
        self.label_display.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_display.setAutoFillBackground(False)
        self.label_display.setText("")
        self.label_display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_display.setObjectName("label_display")
        self.button_7 = QtWidgets.QPushButton(Dialog)
        self.button_7.setGeometry(QtCore.QRect(10, 160, 61, 61))
        self.button_7.setObjectName("button_7")
        self.button_6 = QtWidgets.QPushButton(Dialog)
        self.button_6.setGeometry(QtCore.QRect(150, 230, 61, 61))
        self.button_6.setObjectName("button_6")
        self.button_9 = QtWidgets.QPushButton(Dialog)
        self.button_9.setGeometry(QtCore.QRect(150, 160, 61, 61))
        self.button_9.setObjectName("button_9")
        self.button_5 = QtWidgets.QPushButton(Dialog)
        self.button_5.setGeometry(QtCore.QRect(80, 230, 61, 61))
        self.button_5.setObjectName("button_5")
        self.button_equal = QtWidgets.QPushButton(Dialog)
        self.button_equal.setGeometry(QtCore.QRect(220, 370, 61, 61))
        self.button_equal.setObjectName("button_equal")
        self.button_delete_all = QtWidgets.QPushButton(Dialog)
        self.button_delete_all.setGeometry(QtCore.QRect(10, 90, 61, 61))
        self.button_delete_all.setObjectName("button_delete_all")
        self.button_division = QtWidgets.QPushButton(Dialog)
        self.button_division.setGeometry(QtCore.QRect(220, 90, 61, 61))
        self.button_division.setObjectName("button_division")
        self.button_2 = QtWidgets.QPushButton(Dialog)
        self.button_2.setGeometry(QtCore.QRect(80, 300, 61, 61))
        self.button_2.setObjectName("button_2")
        self.button_1 = QtWidgets.QPushButton(Dialog)
        self.button_1.setGeometry(QtCore.QRect(10, 300, 61, 61))
        self.button_1.setObjectName("button_1")
        self.button_subtraction = QtWidgets.QPushButton(Dialog)
        self.button_subtraction.setGeometry(QtCore.QRect(220, 230, 61, 61))
        self.button_subtraction.setObjectName("button_subtraction")
        self.button_sqrt = QtWidgets.QPushButton(Dialog)
        self.button_sqrt.setGeometry(QtCore.QRect(150, 90, 61, 61))
        self.button_sqrt.setObjectName("button_sqrt")
        self.button_comann = QtWidgets.QPushButton(Dialog)
        self.button_comann.setGeometry(QtCore.QRect(150, 370, 61, 61))
        self.button_comann.setObjectName("button_comann")
        self.button_8 = QtWidgets.QPushButton(Dialog)
        self.button_8.setGeometry(QtCore.QRect(80, 160, 61, 61))
        self.button_8.setObjectName("button_8")
        self.button_delete = QtWidgets.QPushButton(Dialog)
        self.button_delete.setGeometry(QtCore.QRect(80, 90, 61, 61))
        self.button_delete.setObjectName("button_delete")
        self.button_0 = QtWidgets.QPushButton(Dialog)
        self.button_0.setGeometry(QtCore.QRect(10, 370, 131, 61))
        self.button_0.setObjectName("button_0")
        self.button_0.clicked.connect(lambda: print("here"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button_add.setText(_translate("Dialog", "+"))
        self.button_3.setText(_translate("Dialog", "3"))
        self.button_4.setText(_translate("Dialog", "4"))
        self.button_multiple.setText(_translate("Dialog", "*"))
        self.button_7.setText(_translate("Dialog", "7"))
        self.button_6.setText(_translate("Dialog", "6"))
        self.button_9.setText(_translate("Dialog", "9"))
        self.button_5.setText(_translate("Dialog", "5"))
        self.button_equal.setText(_translate("Dialog", "="))
        self.button_delete_all.setText(_translate("Dialog", "C"))
        self.button_division.setText(_translate("Dialog", "÷"))
        self.button_2.setText(_translate("Dialog", "2"))
        self.button_1.setText(_translate("Dialog", "1"))
        self.button_subtraction.setText(_translate("Dialog", "-"))
        self.button_sqrt.setText(_translate("Dialog", "√"))
        self.button_comann.setText(_translate("Dialog", ","))
        self.button_8.setText(_translate("Dialog", "8"))
        self.button_delete.setText(_translate("Dialog", "DEL"))
        self.button_0.setText(_translate("Dialog", "0"))


