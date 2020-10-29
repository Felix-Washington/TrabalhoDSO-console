from controlador.abstract_controlador import AbstractControlador
from entidade.cliente import Cliente
from tela.tela_cliente import TelaCliente

class ControladorCliente(AbstractControlador):
  def __init__(self):
    self.__clientes = [] 
    self.__tela_cliente = TelaCliente()
    self.__controle = True
    self.__opcoes_controle = True
    self.__cliente_logado = None
    self.__log_cliente = True


  def abre_tela(self):
    lista_opcoes = {
    1: self.login_cliente,
    2: self.adiciona, 
    0: self.volta}

    self.limpa_tela()
    self.__controle = True
    while self.__controle:

      opcao_escolhida = self.__tela_cliente.mostra_opcoes()

      funcao_escolhida = lista_opcoes[opcao_escolhida]

      funcao_escolhida()


  def login_cliente(self):
    cpf, senha = self.__tela_cliente.login()

    for um_cliente in self.__clientes:
      if cpf == um_cliente.cpf and senha == um_cliente.senha:
        self.__cliente_logado = um_cliente
        self.cliente_opcoes(um_cliente.nome)
        self.limpa_tela()
      else:
        self.__tela_cliente.avisos("dados_invalidos", "")


  def adiciona(self):
    nome, cpf, senha = self.__tela_cliente.dados_cadastro()
    cliente = Cliente(nome, cpf, senha)
    self.__clientes.append(cliente)
    self.limpa_tela()
    self.__tela_cliente.avisos("cadastrar", "Cliente")


  def volta(self):
    self.__controle = False
    
    self.limpa_tela()
    

  def cliente_opcoes(self, cliente):
    lista_opcoes = {
    1: self.compra,
    2: self.ver_cadastro, 
    3: self.atualiza,
    4: self.remove,
    0: self.desloga}

    self.limpa_tela()
    self.__log_cliente = True
    while self.__log_cliente:

      opcao_escolhida = self.__tela_cliente.tela_cliente_logado(self.__cliente_logado.nome)

      funcao_escolhida = lista_opcoes[opcao_escolhida]

      funcao_escolhida()
  
  
  def compra(self):
    pass


  def ver_cadastro(self):
    self.limpa_tela()
    self.__tela_cliente.tela_mostra_cadastro(
      self.__cliente_logado.nome,
      self.__cliente_logado.cpf,
      self.__cliente_logado.senha)


  def atualiza(self):
    opcao, dado = self.__tela_cliente.tela_atualiza_cadastro()
    self.limpa_tela()
    if opcao == 1:
      self.__cliente_logado.nome = dado
      self.__tela_cliente.avisos("atualiza", "Nome")
    elif opcao == 2:
      self.__cliente_logado.senha = dado
      self.__tela_cliente.avisos("atuazlia", "Senha")

    for um_cliente in self.__clientes:
      if self.__cliente_logado.cpf == um_cliente:
        self.__clientes[um_cliente] = self.__cliente_logado
        
        break
        


  def remove(self):
    cpf, senha = self.__tela_cliente.tela_remove()
    for um_cliente in self.__clientes:
      if cpf != um_cliente.cpf or senha != um_cliente.senha:
        self.__tela_cliente.avisos("dados_invalidos", "")
      elif cpf == um_cliente.cpf and senha == um_cliente.senha:
        self.__clientes.remove(um_cliente)        
        self.limpa_tela()
        self.__tela_cliente.avisos("remover", "cliente")
        self.__log_cliente = False
        break


    
  def desloga(self):
    opcao = self.__tela_cliente.finaliza_tela(
      "pessoa", self.__cliente_logado.nome,)
    if opcao == 1:
      self.__log_cliente = False   
      self.limpa_tela()
