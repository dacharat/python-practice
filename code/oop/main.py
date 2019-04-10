from pet import Pet

pet1 = Pet('Dog', 'ABC')

pet1.call_name()
pet1.sound()

pet1.hit_by_car()
print(pet1.show_number_of_leg())
print(pet1.leg) # ไม่ควรใช้

pet2 = Pet('Cat', 'DEF')
print(pet2)
print(type(pet2))

pet3 = Pet('Cat', 'DEF', 2)
print(pet3.show_number_of_leg())

# =======================================================

from dog import Dog

dog1 = Dog('ABC')
dog1.call_name()
dog1.stand_with_two_leg()
dog1.sound()
