from controlador.abstract_controlador import AbstractControlador

from __tela_produto import TelaProduto

class ControladorProduto(AbstractControlador):

  def __init__(self):
    self.__tela_produto = TelaProduto(self)
    self.__produtos = []

  def inicia(self):
    pass

  def adiciona(self):
    pass

  def remove(self):
    pass

  def atualiza(self):
    pass

  def lista(self):
    pass

  def abre_tela_inicial(self):
    pass
    
  def finaliza_tela(self):
    pass

  def relatorio_estoque(self):
    pass

  def atualiza_estoque(self):
    pass
    
  def imprime_relatorio(self):
    pass
  