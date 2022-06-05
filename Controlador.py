import sys
from math import *
from PyQt5 import QtCore, QtGui, QtWidgets

# Importa interfaces de usuário

import TelaInicial
import CalculadoraSimplesNew
import CalculadoraCientifica
from Model.CalculadoraSimplesModel import CalculadoraSimplesModel


# Cria a classe do controlador

class controller:
    def __init__(self):
        self.num = "0";
        self.result = "";
        self.operacao = "";
        self.operadorClicked = False;
        self.TelaInicial_Window = QtWidgets.QMainWindow()
        self.TelaInicial_ui = TelaInicial.Ui_Dialog()
        self.TelaInicial_ui.setupUi(self.TelaInicial_Window)

        self.tradicional_Window = QtWidgets.QMainWindow()
        self.tradicional_ui = CalculadoraSimplesModel().calc
        self.tradicional_ui.setupUi(self.tradicional_Window)

        self.cientifica_Window = QtWidgets.QMainWindow()
        self.cientifica_ui = CalculadoraCientifica.Ui_Dialog()
        self.cientifica_ui.setupUi(self.cientifica_Window)

        self.TelaInicial_ui.pushButton.clicked.connect(self.show_calc)

        # Define os botões da Calculadora Simples

        self.tradicional_ui.button_0.clicked.connect(lambda: self.setNumBussiness("0"))    # 0
        self.tradicional_ui.button_1.clicked.connect(lambda: self.setNumBussiness("1"))    # 1
        self.tradicional_ui.button_2.clicked.connect(lambda: self.setNumBussiness("2"))     # 2
        self.tradicional_ui.button_3.clicked.connect(lambda:self.setNumBussiness("3"))    # 3
        self.tradicional_ui.button_4.clicked.connect(lambda: self.setNumBussiness("4"))    # 4
        self.tradicional_ui.button_5.clicked.connect(lambda: self.setNumBussiness("5"))    # 5
        self.tradicional_ui.button_6.clicked.connect(lambda: self.setNumBussiness("6"))    # 6
        self.tradicional_ui.button_7.clicked.connect(lambda: self.setNumBussiness("7"))     # 7
        self.tradicional_ui.button_8.clicked.connect(lambda: self.setNumBussiness("8"))     # 8
        self.tradicional_ui.button_9.clicked.connect(lambda: self.setNumBussiness("9"))     # 9
        self.tradicional_ui.button_add.clicked.connect(lambda: self.setOperacao("soma"))  # +
        self.tradicional_ui.button_subtraction.clicked.connect(lambda: self.setOperacao("subtr"))  # -
        self.tradicional_ui.button_multiple.clicked.connect(lambda: self.setOperacao("multi"))   # x
        self.tradicional_ui.button_division.clicked.connect(lambda: self.setOperacao("divi"))   # ÷
        self.tradicional_ui.button_sqrt.clicked.connect(lambda: self.setOperacao("raiz"))   # √
        self.tradicional_ui.button_comann.clicked.connect(lambda: self.setNumBussiness(","))   # ,
        self.tradicional_ui.button_equal.clicked.connect(self.igual)     # =
        self.tradicional_ui.button_delete_all.clicked.connect(self.ac)           # AC
        self.tradicional_ui.button_delete.clicked.connect(self.delete)     # DEL

        # Define os botões da Calculadora Científica

        # self.cientifica_ui.pushButton_43.clicked.connect(self.numero)     # π
        # self.cientifica_ui.pushButton_23.clicked.connect(self.numero)     # 0
        # self.cientifica_ui.pushButton_27.clicked.connect(self.numero)     # 1
        # self.cientifica_ui.pushButton_24.clicked.connect(self.numero)     # 2
        # self.cientifica_ui.pushButton_25.clicked.connect(self.numero)     # 3
        # self.cientifica_ui.pushButton_26.clicked.connect(self.numero)     # 4
        # self.cientifica_ui.pushButton_32.clicked.connect(self.numero)     # 5
        # self.cientifica_ui.pushButton_22.clicked.connect(self.numero)     # 6
        # self.cientifica_ui.pushButton_21.clicked.connect(self.numero)     # 7
        # self.cientifica_ui.pushButton_33.clicked.connect(self.numero)     # 8
        # self.cientifica_ui.pushButton_29.clicked.connect(self.numero)     # 9
        # self.cientifica_ui.pushButton_34.clicked.connect(self.operador)   # +
        # self.cientifica_ui.pushButton_30.clicked.connect(self.operador)   # -
        # self.cientifica_ui.pushButton_38.clicked.connect(self.operador)   # x
        # self.cientifica_ui.pushButton_37.clicked.connect(self.operador)   # ÷
        # self.cientifica_ui.pushButton_35.clicked.connect(self.operador)   # √
        # self.cientifica_ui.pushButton_40.clicked.connect(self.operador)   # x^
        # self.cientifica_ui.pushButton_42.clicked.connect(self.angulo)     # Seno
        # self.cientifica_ui.pushButton_41.clicked.connect(self.angulo)     # Cosseno
        # self.cientifica_ui.pushButton_39.clicked.connect(self.angulo)     # Tangente
        # self.cientifica_ui.pushButton_20.clicked.connect(self.virgula)    # ,
        # self.cientifica_ui.pushButton_28.clicked.connect(self.igual)      # =
        # self.cientifica_ui.pushButton_36.clicked.connect(self.ac)         # AC
        # self.cientifica_ui.pushButton_31.clicked.connect(self.delete)     # DEL
    
    def setNum(self, value, iszero):
        if iszero:
            self.num = value    
            self.tradicional_ui.label_display.setText(self.num)
        else:
            self.num = self.num + value;
            self.tradicional_ui.label_display.setText(self.num)
    
    def setNumBussiness(self, value):
        if not self.operadorClicked:
            self.result=""
        if not self.num.find(",") == -1 and value == ",":
            pass 
        elif self.num == "0" and value == ",":
            self.setNum(value, False)
        elif self.num == "0": 
            self.setNum(value, True)
        else:    
            self.setNum(value, False)
            print(self.num)
    
    def setOperacao(self, value):
        self.result = self.num
        self.num="0"
        self.tradicional_ui.label_display.setText(self.num)
        self.operacao = value
        self.operadorClicked = True 
    

    def delete(self):
        self.tradicional_ui.label_display.setText("0")
        self.cientifica_ui.label.setText(" ")

    def ac(self):
        pass
    
    def igual(self):
        calculator = CalculadoraSimplesModel()
        self.operadorClicked = False
        self.result = calculator.operacao(self.num, self.result, self.operacao)
        self.tradicional_ui.label_display.setText(self.result)
        self.num=""

    def show_TelaInicial(self):
        self.TelaInicial_Window.show()

    def show_calc(self):
        self.tradicional_ui.label_display.setText("0")
        self.cientifica_ui.label.setText(" ")
        self.TelaInicial_Window.close()
        if self.TelaInicial_ui.radioButton.isChecked(): self.tradicional_Window.show()
        else: self.cientifica_Window.show()
            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = controller()
    controller.show_TelaInicial()
    sys.exit(app.exec_())