from controlador.abstract_controlador import AbstractControlador
from tela.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario

class ControladorFuncionario(AbstractControlador):
  def __init__(self):
    self.__funcionarios = []
    self.__tela_funcionario = TelaFuncionario()
    self.__controle = True
    self.__funcionario_logado = None

    self.__log_funcionario = False


  def login_funcionario(self):
    cpf, senha = self.__tela_funcionario.login()
    
    for um_funcionario in self.__funcionarios:
      if cpf == um_funcionario.cpf and senha == um_funcionario.senha:
        self.__funcionario_logado = um_funcionario
        self.funcionario_opcoes(um_funcionario.nome) 
      else:
        self.__tela_funcionario.avisos("dados_invalidos", "")


  def adiciona(self):
    nome, cpf, senha = self.__tela_funcionario.dados_cadastro()
    funcionario = Funcionario(nome, cpf, senha)
    self.__funcionarios.append(funcionario)
    self.limpa_tela()
    self.__tela_funcionario.avisos("cadastrar", "Funcionário")
    

  def remove(self):
    cpf, senha = self.__tela_funcionario.tela_remove()
    for um_funcionario in self.__funcionarios:
      if cpf == um_funcionario.cpf and senha == um_funcionario.senha:
        self.__funcionarios.remove(um_funcionario)
        self.limpa_tela()
        self.__tela_funcionario.avisos("remover", "Funcionario")
        self.__log_funcionario = False
        break


  def ver_estoque(self):
    pass


  def ver_cadastro(self):
    self.limpa_tela()
    self.__tela_funcionario.tela_mostra_cadastro(
    self.__funcionario_logado.nome,
    self.__funcionario_logado.cpf,
    self.__funcionario_logado.senha)


  def atualiza(self):
    pass


  def desloga(self):
    opcao = self.__tela_funcionario.finaliza_tela("pessoa", self.__funcionario_logado.nome)
    if opcao == 1:
      self.__log_funcionario = False
      self.limpa_tela()


  def funcionario_opcoes(self, funcionario):
    lista_opcoes = {
    1: self.ver_estoque,
    2: self.ver_cadastro, 
    3: self.atualiza,
    4: self.remove,
    0: self.desloga}
    
    self.__log_funcionario = True
    self.limpa_tela()
    while self.__log_funcionario:
      opcao_escolhida = self.__tela_funcionario.tela_funcionario_logado(funcionario)
      funcao_escolhida = lista_opcoes[opcao_escolhida]

      funcao_escolhida()


  def abre_tela(self):
    lista_opcoes = {
    1: self.login_funcionario,
    2: self.adiciona, 
    0: self.volta}

    self.limpa_tela()
    self.__controle = True
    while self.__controle:

      opcao_escolhida = self.__tela_funcionario.mostra_opcoes()

      funcao_escolhida = lista_opcoes[opcao_escolhida]

      funcao_escolhida()


  def volta(self):
    self.__controle = False
    self.limpa_tela()
    