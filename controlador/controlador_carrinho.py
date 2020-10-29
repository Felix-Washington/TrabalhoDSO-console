from controlador.abstract_controlador import AbstractControlador
from tela.tela_carrinho import TelaCarrinho

class ControladorCarrinho(AbstractControlador):

  def __init__(self):

    self.__tela_carrinho = TelaCarrinho(self)
    self.__carrinhos = []

  def abre_tela_inicial(self):
    pass

  def inicia (self):
    pass

  def lista(self):
    pass

  def adiciona(self):
    pass

  def remove(self):
    pass

  def atualiza(self):
    pass

  def limpa_tela(self):
    pass

  def limpar_carrinho(self):
    pass
    
  def valor_total(self):
    pass

  def finaliza_tela(self):
    pass

 


  