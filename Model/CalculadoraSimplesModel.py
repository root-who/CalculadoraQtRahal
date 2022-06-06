import string
import CalculadoraSimples
from math import *

class CalculadoraSimplesModel():
    def __init__(self):
        self.calc = CalculadoraSimples.Ui_Dialog()
              
    def soma(self, num1:str, num2:str):
        return str("{:.3f}".format(float(num1) + float(num2)))
 
    def divisao(self, num1:str, num2:str):
        if num2 == 0 : return "ERROR"
        return str("{:.3f}".format(float(num1) / float(num2)))
    
    def multiplicacao(self, num1:str, num2:str):
        return str("{:.3f}".format(float(num1) * float(num2)))
    
    def subtracao(self, num1:str, num2:str):
        return str("{:.3f}".format(float(num1) - float(num2)))

    def raiz(self, num1:str):
        return str("{:.3f}".format(sqrt(float(num1))))

    def operacao(self, num1:str, num2:str, operacao:str):
        if operacao == "soma": return self.soma(num1, num2) 
        if operacao == "divi": return self.divisao(num1, num2)
        if operacao == "multi": return self.multiplicacao(num1, num2)
        if operacao == "subtr": return self.subtracao(num1, num2)
    