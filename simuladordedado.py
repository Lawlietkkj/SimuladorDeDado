# ISSO VAI SIMULAR UM DADO
# SIMULAR O USO DE UM DADO, GERANDO VALOR DE 1 ATE 6 
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('Não')]
        ]

    def Iniciar(self):
        # janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
        # valores da tela
        self.eventos, self.valores = self.janela.Read()
        # valores fucionando
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Agrecemos a sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')
    
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()