class Player :
  def __init__(self, p_number, symbol) :
    self.symbol = symbol
    self.p_number = p_number

  def getPlayerNumber(self) :
    return self.p_number

  def getSymbol(self) :
    return self.symbol