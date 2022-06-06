import sys
from math import *
from Model.CalculadoraCientificaModel import CalculadoraCientificaModel
from PyQt5 import QtCore, QtGui, QtWidgets
import TelaInicial
import CalculadoraSimples
import CalculadoraCientifica
from Model.CalculadoraSimplesModel import CalculadoraSimplesModel

# Cria a classe do controlador

class controller:
    def __init__(self):
        self.num1 = "0";
        self.num2 = "0";
        self.result = "0";
        self.operacao = "";
        self.operadorClicked = False;
        self.TelaInicial_Window = QtWidgets.QMainWindow()
        self.TelaInicial_ui = TelaInicial.Ui_Dialog()
        self.TelaInicial_ui.setupUi(self.TelaInicial_Window)
        self.calculatorSimples = CalculadoraSimplesModel()
        self.calculatorCientifica = CalculadoraCientificaModel()
        self.tradicional_Window = QtWidgets.QMainWindow()
        self.tradicional_ui = self.calculatorSimples.calc
        self.tradicional_ui.setupUi(self.tradicional_Window)

        self.cientifica_Window = QtWidgets.QMainWindow()
        self.cientifica_ui = self.calculatorCientifica.calc
        self.cientifica_ui.setupUi(self.cientifica_Window)

        self.TelaInicial_ui.pushButton.clicked.connect(self.show_calc)

        # Define os botões da Calculadora Simples

        self.tradicional_ui.button_0.clicked.connect(lambda: self.isOperatorClicked("0"))    # 0
        self.tradicional_ui.button_1.clicked.connect(lambda: self.isOperatorClicked("1"))    # 1
        self.tradicional_ui.button_2.clicked.connect(lambda: self.isOperatorClicked("2"))     # 2
        self.tradicional_ui.button_3.clicked.connect(lambda: self.isOperatorClicked("3"))    # 3
        self.tradicional_ui.button_4.clicked.connect(lambda: self.isOperatorClicked("4"))    # 4
        self.tradicional_ui.button_5.clicked.connect(lambda: self.isOperatorClicked("5"))    # 5
        self.tradicional_ui.button_6.clicked.connect(lambda: self.isOperatorClicked("6"))    # 6
        self.tradicional_ui.button_7.clicked.connect(lambda: self.isOperatorClicked("7"))     # 7
        self.tradicional_ui.button_8.clicked.connect(lambda: self.isOperatorClicked("8"))     # 8
        self.tradicional_ui.button_9.clicked.connect(lambda: self.isOperatorClicked("9"))     # 9
        self.tradicional_ui.button_add.clicked.connect(lambda: self.setOperacao("soma"))  # +
        self.tradicional_ui.button_subtraction.clicked.connect(lambda: self.setOperacao("subtr"))  # -
        self.tradicional_ui.button_multiple.clicked.connect(lambda: self.setOperacao("multi"))   # x
        self.tradicional_ui.button_division.clicked.connect(lambda: self.setOperacao("divi"))   # ÷
        self.tradicional_ui.button_sqrt.clicked.connect(lambda: self.operacaoSimples("raiz"))   # √
        self.tradicional_ui.button_comann.clicked.connect(lambda: self.isOperatorClicked(","))   # ,
        self.tradicional_ui.button_equal.clicked.connect(lambda: self.igual())     # =
        self.tradicional_ui.button_delete_all.clicked.connect(self.ac)           # AC
        self.tradicional_ui.button_delete.clicked.connect(self.delete)     # DEL

        # Define os botões da Calculadora Científica

        self.cientifica_ui.pushButton_43.clicked.connect(lambda: self.isOperatorClicked("0"))     # π
        self.cientifica_ui.pushButton_23.clicked.connect(lambda: self.isOperatorClicked("0"))     # 0
        self.cientifica_ui.pushButton_27.clicked.connect(lambda: self.isOperatorClicked("1"))     # 1
        self.cientifica_ui.pushButton_24.clicked.connect(lambda: self.isOperatorClicked("2"))     # 2
        self.cientifica_ui.pushButton_25.clicked.connect(lambda: self.isOperatorClicked("3"))     # 3
        self.cientifica_ui.pushButton_26.clicked.connect(lambda: self.isOperatorClicked("4"))     # 4
        self.cientifica_ui.pushButton_32.clicked.connect(lambda: self.isOperatorClicked("5"))     # 5
        self.cientifica_ui.pushButton_22.clicked.connect(lambda: self.isOperatorClicked("6"))     # 6
        self.cientifica_ui.pushButton_21.clicked.connect(lambda: self.isOperatorClicked("7"))     # 7
        self.cientifica_ui.pushButton_33.clicked.connect(lambda: self.isOperatorClicked("8"))     # 8
        self.cientifica_ui.pushButton_29.clicked.connect(lambda: self.isOperatorClicked("9"))     # 9
        self.cientifica_ui.pushButton_34.clicked.connect(lambda: self.setOperacao("soma"))   # +
        self.cientifica_ui.pushButton_30.clicked.connect(lambda: self.setOperacao("subtr"))   # -
        self.cientifica_ui.pushButton_38.clicked.connect(lambda: self.setOperacao("multi"))   # x
        self.cientifica_ui.pushButton_37.clicked.connect(lambda: self.setOperacao("divi"))   # ÷
        self.cientifica_ui.pushButton_35.clicked.connect(lambda: self.operacaoSimples("raiz"))   # √
        self.cientifica_ui.pushButton_40.clicked.connect(lambda: self.operacaoSimples("pot"))   # x^
        self.cientifica_ui.pushButton_42.clicked.connect(lambda: self.operacaoSimples("sin"))     # Seno
        self.cientifica_ui.pushButton_41.clicked.connect(lambda: self.operacaoSimples("cos"))     # Cosseno
        self.cientifica_ui.pushButton_39.clicked.connect(lambda: self.operacaoSimples("tan"))     # Tangente
        self.cientifica_ui.pushButton_20.clicked.connect(lambda: self.isOperatorClicked(","))    # ,
        self.cientifica_ui.pushButton_28.clicked.connect(lambda: self.igual())      # =
        self.cientifica_ui.pushButton_36.clicked.connect(self.ac)         # AC
        self.cientifica_ui.pushButton_31.clicked.connect(self.delete)     # DEL
    
    def setNum2(self, value, iszero):
        if iszero:
            self.num2 = value    
            self.tradicional_ui.label_display.setText(self.num2)
            self.cientifica_ui.label.setText(self.num2)
        else:
            self.num2 = self.num2 + value;
            self.tradicional_ui.label_display.setText(self.num2)
            self.cientifica_ui.label.setText(self.num2)
            
    def setNum1(self, value, iszero):
        if iszero:
            self.num1 = value    
            self.tradicional_ui.label_display.setText(self.num1)
            self.cientifica_ui.label.setText(self.num1)
        else:
            self.num1 = self.num1 + value;
            self.tradicional_ui.label_display.setText(self.num1)
            self.cientifica_ui.label.setText(self.num1)
            
 
    def isOperatorClicked(self, value):
        print("aqui " + str(self.operadorClicked))
        if self.operadorClicked:
            self.setNumBussiness(self.num2, value, True)
        else: self.setNumBussiness(self.num1, value, False)
    
        print(self.num1 + " " + self.num2)
            
    def setNumBussiness(self, var, value, funcao):
        if not var.find(",") == -1 and value == ",":
                pass 
        elif var == "0" and value == ",":
            if funcao : self.setNum2(value, False) 
            else: self.setNum1(value, False)
        elif var == "0": 
             if funcao : self.setNum2(value, True)
             else: self.setNum1(value, True)
        else:    
            if funcao : self.setNum2( value, False)
            else: self.setNum1( value, False)


    def operacaoSimples(self, operacao):
        if self.result == "0":
            self.result = self.calculatorCientifica.operacao(self.num1, operacao)
            self.tradicional_ui.label_display.setText(self.result)
            self.cientifica_ui.label.setText(self.result)
            self.num1="0"
        else:
            self.result = self.calculatorCientifica.operacao(self.result, operacao)
            self.tradicional_ui.label_display.setText(self.result)
            self.cientifica_ui.label.setText(self.result)
            self.num1="0"
        
        
    def setOperacao(self, value):
        
        if self.operadorClicked == True and self.result != "0":
            self.igualOperacaoAgregada(self.result, self.num2)

            self.operacao = value
        elif self.operadorClicked == True and self.result == "0":
            self.igualOperacaoAgregada(self.num1, self.num2)
            self.operacao = value
        else:
            self.operacao = value
            self.operadorClicked = True 
    
    
    def delete(self):
        self.tradicional_ui.label_display.setText("0")
        self.cientifica_ui.label.setText("0")

    def ac(self):
        pass
    
    def igualOperacaoAgregada(self, num1, num2):
        self.result = self.calculatorSimples.operacao(num1, num2, self.operacao)
        self.tradicional_ui.label_display.setText(self.result)
        self.cientifica_ui.label.setText(self.result)
        print("NUM1 "+num1)
        print("NUM2 "+num2)
        print("RESULTADO " + self.result)
        self.num1="0"
        self.num2="0"
    
    def igual(self):
        self.operadorClicked = False
        if self.result == "0":
            self.result = self.calculatorSimples.operacao(self.num1, self.num2, self.operacao)
            self.tradicional_ui.label_display.setText(self.result)
            self.cientifica_ui.label.setText(self.result)
        else: 
            self.result = self.calculatorSimples.operacao(self.result, self.num2, self.operacao)
            self.tradicional_ui.label_display.setText(self.result)
            self.cientifica_ui.label.setText(self.result)
        print("NUM1 "+self.num1)
        print("NUM2 "+self.num2)
        print("RESULTADO " + self.result)
        self.num1="0"
        self.num2="0"

    def show_TelaInicial(self):
        self.TelaInicial_Window.show()

    def show_calc(self):
        self.tradicional_ui.label_display.setText("0")
        self.cientifica_ui.label.setText("0")
        self.TelaInicial_Window.close()
        if self.TelaInicial_ui.radioButton.isChecked(): self.tradicional_Window.show()
        else: self.cientifica_Window.show()
            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = controller()
    controller.show_TelaInicial()
    sys.exit(app.exec_())