class Pet :
  def __init__(self, species, name, leg = 4):
    self.species = species
    self.name = name
    self.leg = leg
  
  def call_name(self) :
    print(self.name)

  def sound(self) :
    if self.species == 'Dog' :
      print('Hong Hong')
    elif self.species == 'Cat' :
      print('Meow Meow')
    else :
      print('----------')
  
  def hit_by_car(self):
    self.leg -= 1

  def show_number_of_leg(self) :
    return self.leg