from abc import ABC, abstractmethod
import os

class AbstractControlador(ABC):
  def __init__(self):
    pass

  @abstractmethod
  def adiciona(self):
    pass

  @abstractmethod
  def remove(self):
    pass

  @abstractmethod
  def atualiza(self):
    pass

  def lista(self):
    pass

  def limpa_tela(self):
    os.system('cls' if os.name == 'nt' else 'clear')