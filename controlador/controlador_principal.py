from controlador.controlador_cliente import ControladorCliente
from controlador.controlador_funcionario import ControladorFuncionario



from tela.tela_principal import TelaPrincipal


class ControladorPrincipal():
  def __init__(self):
    self.__controlador_cliente = ControladorCliente()
    self.__controlador_funcionario = ControladorFuncionario()
    self.__tela_principal = TelaPrincipal(self)


  def inicia_sistema(self):
    self.__tela_principal.avisos("inicia", "")
    self.abre_tela_inicial()


  def mostra_tela_funcionario(self):
    self.__controlador_funcionario.abre_tela_inicial()


  def mostra_tela_cliente(self):
    self.__controlador_cliente.abre_tela_inicial()

  def abre_tela_inicial(self):
    lista_opcoes = {
    1: self.mostra_tela_funcionario,
    2: self.mostra_tela_cliente, 
    0: self.fecha_sistema}

    while self.__controle:
  
      opcao_escolhida = self.__tela_principal.mostra_opcoes()
      
      funcao_escolhida = lista_opcoes[opcao_escolhida]

      funcao_escolhida()
    def finaliza_sistema(self):
    pass
  