from tela.abstract_tela import AbstractTela

class TelaCliente(AbstractTela):
  def __init__(self):
    pass


  def dados_cadastro(self):
    print("Digite seu nome:")
    nome = self.verifica_palavra()

    print("Digite seu CPF")
    cpf = self.verifica_inteiro("O CPF")

    print("Digite a sua senha")
    senha = input("")

    return nome, cpf, senha


  def login(self):    
    print("Digite seu CPF:")
    cpf = self.verifica_inteiro("O CPF")
    print("Digite sua senha:")
    senha = input()

    return cpf, senha


  def tela_remove(self):
    print("Digite seu CPF:")
    cpf = self.verifica_inteiro("O CPF")
    print("Digite sua senha:")
    senha = input("")

    print("Tem certeza que deseja remover o cadastro?")
    print("1 - Sim")
    print("2 - Não")
    opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2])

    if opcao == 1:
      return cpf, senha
    elif opcao == 2:
      return 0, 0


  def tela_atualiza_cadastro(self):
    print("O que você quer alterar?")
    print("1 - Nome")
    print("2 - Senha")
    print("0 - Voltar")
    
    opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 0])

    if opcao == 1:
      print("Digite seu novo nome: ")
      dado = self.verifica_palavra()

    elif opcao == 2:
      print("Digite sua nova senha:")
      dado = input()

    return opcao, dado
    

  def tela_mostra_cadastro(self, nome, cpf, senha):
    print("Nome:", nome.lower().capitalize())
    print("CPF:", cpf)
    print("Senha:", senha)
    print("")


  def tela_cliente_logado(self, nome_cliente: str):
    print("Ola", nome_cliente.lower().capitalize(), "o que você deseja?")
    print("1 - Comprar")
    print("2 - Ver Cadastro")
    print("3 - Alterar Cadastro")
    print("4 - Remover Cadastro")
    print("0 - Sair")

    opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 0])
    return opcao


  def mostra_opcoes(self):
    print("Como cliente você deseja:")
    print("1 - Logar")
    print("2 - Cadastrar")
    print("0 - Voltar")

    opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 0])
    return opcao






