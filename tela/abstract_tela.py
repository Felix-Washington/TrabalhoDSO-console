from abc import ABC, abstractmethod

class AbstractTela(ABC):
  @abstractmethod
  def __init__():
    pass

  def le_numero_inteiro(self, mensagem: str, opcoes_validas: []):
    while True:
      valor_lido = input(mensagem)
      try:
        inteiro = int(valor_lido)
        if inteiro not in opcoes_validas:
          raise ValueError
        return inteiro
      except ValueError:
        print("Digite uma opção válida!")


  def verifica_inteiro(self, entidade: str):
    while True:
      valor = input()
      
      try:
        inteiro = int(valor)
        if type(inteiro) != int:
          raise ValueError

        return valor
      except ValueError:
        print(entidade ,"deve ser composto apenas de números inteiros!")


  def verifica_palavra(self):
    while True:
      valor = input()
      
      try:
        ha_numero = any(char.isdigit() for char in valor)

        if ha_numero:
          raise ValueError
        else:
          return valor
      except ValueError:
        print("Digite apenas letras!")



  @abstractmethod
  def mostra_opcoes(self):
    pass


  def avisos(self, opcao: str, entidade: str):
    if opcao == "cadastrar":
      print(entidade, "cadastrado com sucesso!")
    elif opcao == "remover":
      print(entidade, "removido com sucesso!")
    elif opcao == "dados_invalidos":
      print("Erro! Digite o cpf ou a senha corretamente!")
    elif opcao == "finalizar":
      print("Sistema Encerrado!")
    elif opcao == "inicia":
      print("Bem vindo a loja de brinquedos!")

    elif opcao == "atualiza":
      print(entidade, "alterado com sucesso!")


  def finaliza_tela(self, entidade: str, nome: str):
    if entidade == "pessoa":
      print(nome.lower().capitalize(), "tem certeza que deseja sair da sua conta?")

    elif entidade == "menu":
      print("Tem certeza que quer fechar o sistema?")

    elif entidade == "atualiza":
      print("Tem certeza que deseja mudar", nome)

    elif entidade == "volta":
      print("Tem certeza que deseja voltar?")

    print("1 - Sim")
    print("2 - Não")
    opcao = self.le_numero_inteiro("", [1, 2])

    return opcao