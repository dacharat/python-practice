from pet import Pet

class Dog(Pet):
  def __init__(self, name) :
    super().__init__("Dog", name)

  def stand_with_two_leg(self) :
    print('Standing with 2 legs')

  def sound(self) :
    print('Haha')