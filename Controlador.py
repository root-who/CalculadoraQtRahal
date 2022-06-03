import sys
from math import *
from PyQt5 import QtCore, QtGui, QtWidgets

# Importa interfaces de usuário

import TelaInicial
import CalculadoraSimples
import CalculadoraCientifica

# Cria a classe do controlador

class controller:
    def __init__(self):
        self.TelaInicial_Window = QtWidgets.QMainWindow()
        self.TelaInicial_ui = TelaInicial.Ui_Dialog()
        self.TelaInicial_ui.setupUi(self.TelaInicial_Window)

        self.tradicional_Window = QtWidgets.QMainWindow()
        self.tradicional_ui = CalculadoraSimples.Ui_Dialog()
        self.tradicional_ui.setupUi(self.tradicional_Window)

        self.cientifica_Window = QtWidgets.QMainWindow()
        self.cientifica_ui = CalculadoraCientifica.Ui_Dialog()
        self.cientifica_ui.setupUi(self.cientifica_Window)

        self.TelaInicial_ui.pushButton.clicked.connect(self.show_calc)

        # Define os botões da Calculadora Simples

        self.tradicional_ui.pushButton_18.clicked.connect(self.numero)    # 0
        self.tradicional_ui.pushButton_15.clicked.connect(self.numero)    # 1
        self.tradicional_ui.pushButton_14.clicked.connect(self.numero)    # 2
        self.tradicional_ui.pushButton_16.clicked.connect(self.numero)    # 3
        self.tradicional_ui.pushButton_9.clicked.connect(self.numero)     # 4
        self.tradicional_ui.pushButton_11.clicked.connect(self.numero)    # 5
        self.tradicional_ui.pushButton_12.clicked.connect(self.numero)    # 6
        self.tradicional_ui.pushButton_5.clicked.connect(self.numero)     # 7
        self.tradicional_ui.pushButton_7.clicked.connect(self.numero)     # 8
        self.tradicional_ui.pushButton_8.clicked.connect(self.numero)     # 9
        self.tradicional_ui.pushButton_13.clicked.connect(self.operador)  # +
        self.tradicional_ui.pushButton_10.clicked.connect(self.operador)  # -
        self.tradicional_ui.pushButton_6.clicked.connect(self.operador)   # x
        self.tradicional_ui.pushButton_4.clicked.connect(self.operador)   # ÷
        self.tradicional_ui.pushButton_3.clicked.connect(self.operador)   # √
        self.tradicional_ui.pushButton_19.clicked.connect(self.virgula)   # ,
        self.tradicional_ui.pushButton_17.clicked.connect(self.igual)     # =
        self.tradicional_ui.pushButton.clicked.connect(self.ac)           # AC
        self.tradicional_ui.pushButton_2.clicked.connect(self.delete)     # DEL

        # Define os botões da Calculadora Científica

        self.cientifica_ui.pushButton_43.clicked.connect(self.numero)     # π
        self.cientifica_ui.pushButton_23.clicked.connect(self.numero)     # 0
        self.cientifica_ui.pushButton_27.clicked.connect(self.numero)     # 1
        self.cientifica_ui.pushButton_24.clicked.connect(self.numero)     # 2
        self.cientifica_ui.pushButton_25.clicked.connect(self.numero)     # 3
        self.cientifica_ui.pushButton_26.clicked.connect(self.numero)     # 4
        self.cientifica_ui.pushButton_32.clicked.connect(self.numero)     # 5
        self.cientifica_ui.pushButton_22.clicked.connect(self.numero)     # 6
        self.cientifica_ui.pushButton_21.clicked.connect(self.numero)     # 7
        self.cientifica_ui.pushButton_33.clicked.connect(self.numero)     # 8
        self.cientifica_ui.pushButton_29.clicked.connect(self.numero)     # 9
        self.cientifica_ui.pushButton_34.clicked.connect(self.operador)   # +
        self.cientifica_ui.pushButton_30.clicked.connect(self.operador)   # -
        self.cientifica_ui.pushButton_38.clicked.connect(self.operador)   # x
        self.cientifica_ui.pushButton_37.clicked.connect(self.operador)   # ÷
        self.cientifica_ui.pushButton_35.clicked.connect(self.operador)   # √
        self.cientifica_ui.pushButton_40.clicked.connect(self.operador)   # x^
        self.cientifica_ui.pushButton_42.clicked.connect(self.angulo)     # Seno
        self.cientifica_ui.pushButton_41.clicked.connect(self.angulo)     # Cosseno
        self.cientifica_ui.pushButton_39.clicked.connect(self.angulo)     # Tangente
        self.cientifica_ui.pushButton_20.clicked.connect(self.virgula)    # ,
        self.cientifica_ui.pushButton_28.clicked.connect(self.igual)      # =
        self.cientifica_ui.pushButton_36.clicked.connect(self.ac)         # AC
        self.cientifica_ui.pushButton_31.clicked.connect(self.delete)     # DEL
    
    # Métodos
    def porcentagem(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()

        # texto=str(float(texto)/100)
        if(texto == " " or texto.endswith(("+", "-", "*", "√", "÷", "(", " ", "%","a"))):
            envia = texto
        elif(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9","π",")"))):
            envia = texto+"%"
        elif(texto.endswith(",")):
            envia = texto+"0%"
        else:
            envia = texto

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def operador(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
            sender = self.tradicional_Window.sender().text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()
            sender = self.cientifica_Window.sender().text()
        
        if(sender=="√"):
            if(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9","π",")","%"))):
                envia = texto + "*√("
            elif(texto.endswith(("+", "-", "*", "÷", " ","("))):
                envia = texto + "√("
            elif(texto.endswith(",")):
                envia = texto + "0*√("
            elif(texto.endswith("a")):
                envia = texto
        elif(sender=="x^"):
            if(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9","π",")","%"))):
                envia = texto + "^("
            elif(texto.endswith(("+", "-", "*", "÷", " ","("))):
                envia = texto
            elif(texto.endswith(",")):
                envia = texto + "0^("
            elif(texto.endswith("a")):
                envia = texto
        elif(texto.endswith(("+", "-", "*", "÷"))):
            if(texto[len(texto)-2]=="(" and sender in ["+","-"]):
                envia = texto[0:len(texto)-1]+sender
            elif(texto[:len(texto)-1].endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",")","π")) or texto[len(texto)-2]=="%"):
                envia = texto[0:len(texto)-1]+sender
            else:
                envia = texto
        elif(texto.endswith(",")):
            envia = texto + "0" + sender
        elif(texto.endswith("(")):
            if(sender in ["+", "-"]):
                envia = texto + sender
            else:
                envia = texto
        elif(texto == " " or texto.endswith("a")):
            envia = texto
        else:
            envia = texto + sender
        
        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def virgula(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()
        if(texto == " " or texto.endswith(("+", "-", "*", "√", "÷", "("))):
            envia = texto+"0,"
        elif(texto.endswith("%")):
            envia = texto+"*0,"
        elif(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9","π"))):
            index = max(texto.rfind("+"), texto.rfind("-"), texto.rfind("*"), texto.rfind("÷"), texto.rfind("√"), texto.rfind("^"))+1
            if(texto[index:].find(",")==-1):
                envia=texto+","
            else:
                envia=texto
        elif(texto.endswith(",")):
            envia = texto
        elif(texto.endswith("a")):
            envia = texto
        else:
            envia = texto

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def abre(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()

        if(texto.endswith(("+", "-", "*", "÷", "√", "(", " "))):
            envia = texto+"("
        elif(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")","π"))):
            envia = texto+"*("
        elif(texto.endswith(",")):
            envia = texto+"0*("
        elif(texto.endswith("a")):
            envia = texto
        else:
            envia = texto

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def fecha(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()

        contab = texto.count("(")
        contfe = texto.count(")")
        if(contab-contfe == 0 or texto.endswith(("+", "-", "*", "÷", "(", " "))):
            envia = texto
        elif(texto.endswith(",")):
            envia = texto + "0)"
        elif(contab-contfe >= 1):
            envia = texto+")"
        elif(texto.endswith("a")):
            envia = texto
        else:
            envia = texto

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def angulo(self):
        texto = self.cientifica_ui.label.text()
        sender = self.cientifica_Window.sender().text()

        if(texto.endswith(("+", "-", "*", "÷", "(", " ", "a"))):
            envia = texto+sender+"("
        elif(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")","π"))):
            envia = texto+"*"+sender+"("
        else:
            envia = texto+sender+"("

        self.cientifica_ui.label.setText(envia)

    def arco(self):
        texto = self.cientifica_ui.label.text()
        if(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")","π"))):
            envia=texto+"*a"
        elif(texto.endswith(("+", "-", "*", "÷", "(", " "))):
            envia=texto+"a"
        elif(texto.endswith("a")):
            envia=texto
        self.cientifica_ui.label.setText(envia)

    def numero(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
            sender = self.tradicional_Window.sender().text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()
            sender = self.cientifica_Window.sender().text()

        if(texto.endswith(")")):
            envia = texto + "*" + sender
        elif(texto.endswith("a")):
            envia=texto
        else:
            envia = texto+sender

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def igual(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()

        contab = texto.count("(")
        contfe = texto.count(")")
        if(contab-contfe >= 1):
            texto = texto+")"*(contab-contfe)

        texto = texto.replace(",",".").replace("e","i").replace("√","sqrt").replace("^","**").replace("÷","/").replace("π","pi")
        try:
            aux = eval(texto)
            envia = str(float(f'{aux:.3f}')).replace(".",",")
        except (NameError, ValueError, SyntaxError):
            envia = texto.replace(".",",").replace("pi","π").replace("i","e").replace("sqrt","√").replace("**","^").replace("/","÷")
            QtWidgets.QMessageBox.about(self.cientifica_Window, "Math domain error", "Raízes negativas não são permitidas\nArcos (seno e cosseno) são calculados para valores entre -1 e +1")

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def delete(self):
        # Calculadora tradicional
        self.tradicional_ui.label.setText(" ")

        # Calculadora científica
        self.cientifica_ui.label.setText(" ")

    def ac(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()
        
        envia = texto[0:len(texto)-1]
        if(texto == " "):
            envia = " "
        elif(texto.endswith("(") and texto[:len(texto)-1].endswith(("√", "^"))):
            envia = texto[0:len(texto)-2]
        elif(texto.endswith("(") and texto[:len(texto)-1].endswith(("n", "s"))):
            envia = texto[0:len(texto)-4]

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def show_TelaInicial(self):
        self.TelaInicial_Window.show()

    def show_calc(self):
        self.tradicional_ui.label.setText(" ")
        self.cientifica_ui.label.setText(" ")
        if self.TelaInicial_ui.radioButton.isChecked():
            self.tradicional_Window.show()
            self.TelaInicial_Window.close()

        if self.TelaInicial_ui.radioButton_2.isChecked():
            self.cientifica_Window.show()
            self.TelaInicial_Window.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = controller()
    controller.show_TelaInicial()
    sys.exit(app.exec_())