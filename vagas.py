class EdificioGaragem:
  def NomeEG(self):
    return "Edificio Garagem"
  
  def VagasEG(self):
    return 300

  def ValorEG(self):
    return 1.50

class EstacionamentoExterno:
  def NomeExt(self):
    return "Estacionamento Externo"
  
  def VagasExt(self):
    return 175

  def ValorExt(self):
    return 1.00

class Adapter:
  def __init__(self, nome, vagas, valor, **adaptedMethods):
    self.nome = nome
    self.vagas = vagas
    self.valor = valor
    self.__dict__.update(adaptedMethods)

  def __getattr__(self, attr):
    return getattr(self.nome, self.vagas, self.valor, attr)

  def originalDict(self):
    return self.vagas.__dict__
    return self.valor.__dict__