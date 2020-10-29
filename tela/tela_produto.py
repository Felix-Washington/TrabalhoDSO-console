from tela.abstract_tela import AbstractTela

class TelaProduto(AbstractTela):
  def __init__(self):
    pass


  def mostra_opcoes(self):
    print("Você deseja:")
    print("1 - Cadastrar Produto")
    print("2 - Remover Produto")
    print("3 - Remover Cadastro")
    print("0 - Voltar")