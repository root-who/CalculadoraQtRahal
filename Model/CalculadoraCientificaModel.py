import string
import CalculadoraCientifica
from math import *
from Model.CalculadoraSimplesModel import CalculadoraSimplesModel

class CalculadoraCientificaModel(CalculadoraSimplesModel):
    def __init__(self):
        self.calc = CalculadoraCientifica.Ui_Dialog()
              
    def potencia(self, num1:str, num2:str):
        return str("{:.3f}".format(float(num1) ** float(num2)))
 
    def consseno(self, num1:str):
        return str("{:.3f}".format(cos(float(num1))))
    
    def seno(self, num1:str):
        return str("{:.3f}".format(sin(float(num1))))
    
    def tangente(self, num1:str):
        return str("{:.3f}".format(tan(float(num1))))


    def operacao(self, num1:str, operacao:str):
        if operacao == "cos": return self.consseno(num1) 
        if operacao == "sin": return self.seno(num1)
        if operacao == "tan": return self.tangente(num1)
        if operacao == "pot": return self.subtracao(num1, 2)
    