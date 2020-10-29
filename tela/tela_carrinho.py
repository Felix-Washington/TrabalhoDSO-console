from tela.abstract_tela import AbstractTela

class TelaCarrinho(AbstractTela)

  def __init__(self, controlador):
    self.__controlador = controlador

  def mostra_opcoes(self):
    print("------ REALIZAR COMPRA ------")
    print("1 - Listar produtos disponíveis")
    print("2 - Adicionar produto")
    print("3 - Remover produto")
    print("4 - Atualizar quantidade")
    print("5 - Limpar carrinho")
    print("6 - Finalizar compra")
    print("0 - Voltar")
    
    opcao = self.le_numero_inteiro("Escolha a opção: ")
    return opcao

  def avisos(self):
    pass