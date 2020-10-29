from tela.abstract_tela import AbstractTela

class TelaProduto(AbstractTela):
    def __init__(self, controlador):
      self.__controlador = controlador

    def mostra_opcoes(self):
      
      print("------ PRODUTO ------")
      print("1 - Adicionar Produto")
      print("2 - Remover Produto")
      print("3 - Atualizar Produto")
      print("4 - Listar Produtos")
      print("5 - Imprimir Relatório de Estoque")
      print("0 - Voltar")
    
      opcao = self.le_numero_inteiro("Escolha a opção: ")
      return opcao
    def avisos(self):
      pass