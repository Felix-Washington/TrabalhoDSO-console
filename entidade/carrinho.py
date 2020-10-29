

class Carrinho:

  def __init__(self):
    self.__quantidade = 0


  @property
  def quantidade(self):
    return self.__quantidade


  @quantidade.setter
  def quantidade(self, quantidade):
    self.__quantidade = quantidade

  