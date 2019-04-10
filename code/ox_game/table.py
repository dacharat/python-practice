class Table :
  def __init__(self, size, nb_of_players, sym_list) :
    self.size = size
    self.currentTable = [['.' for i in range(size)] for j in range(size)]
    self.nb_of_players = nb_of_players
    self.sym_list = sym_list

  def printTable(self) :
    for i in range(self.size) :
      for j in range(self.size) :
        print(self.currentTable[i][j], end=' ')
      print()

  def updateTable(self, row, column, symbol) :
    self.currentTable[row][column] = symbol 

  def play(self) :
    isEnd = False
    p_turn = 0
    print('Input row and column with "," between them(Ex. 1,1)')
    while not isEnd:
      p_number = p_turn % self.nb_of_players
      position = input(f'player{p_number+1} select place to fill your symbol({self.sym_list[p_number]}): ')
      index = [i.strip() for i in position.split(',')]

      if(self.currentTable[int(index[0])][int(index[1])] != '.') :
        print('This position alreay used!!')
        continue

      self.updateTable(int(index[0]), int(index[1]), self.sym_list[p_number])
      self.printTable()

      if(self.checkWinner()) :
        break

      p_turn += 1
    return p_number+1

  def checkWinner(self) :
    # print(f'vertical: {self.verticalWinCheck()}')
    # print(f'horizontal: {self.horizontalWinCheck()}')
    # print(f'diagonal: {self.diagonalWinCheck()}')
    return self.verticalWinCheck() or self.horizontalWinCheck() or self.diagonalWinCheck()

  def verticalWinCheck(self) :
    for i in range(self.size-2) :
      for j in range(self.size) :
        if(self.currentTable[i][j] != '.' and self.currentTable[i][j] == self.currentTable[i+1][j] == self.currentTable[i+2][j]) :
          return True
    return False

  def horizontalWinCheck(self) :
    for i in range(self.size) :
      for j in range(self.size - 2) :
        if(self.currentTable[i][j] != '.' and self.currentTable[i][j] == self.currentTable[i][j+1] == self.currentTable[i][j+2]) :
          return True
    return False
  
  def diagonalWinCheck(self) :
    for i in range(self.size - 2) :
      for j in range(self.size - 2) :
        if(self.currentTable[i][j] != '.' and self.currentTable[i][j] == self.currentTable[i+1][j+1] == self.currentTable[i+2][j+2]) :
          return True
    return False
