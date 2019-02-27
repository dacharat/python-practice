# วาดตรงไม้
import math

n = int(input("n = "))

def normalTree(n) :
  for i in range(n) :
    space = n - i - 1
    star = 2 * i + 1
    # for y in range(n-i) :
    #   print(" ", end="")
    # for y in range(i*2 - 1) :  
    #   print("*", end="")
    # print()
    print(" "*space+"*"*star)
  base = math.ceil(n / 2)
  for i in range(base):
    for y in range(n-1):
      print(" ", end="")
    print("*")

def downTree(n) :
  base = math.ceil(n / 2)
  for i in range(base):
    for y in range(n-1):
      print(" ", end="")
    print("*")
  for i in range(n-1,-1,-1) :
    space = n - i -1
    star = 2 * i + 1
    print(" "*space + "*"*star)

def rightTree(n) :
  base = math.ceil(n / 2)
  for i in range(1,n) : 
    print("  "*base + "* "*i)
  print("* "*(base + n))
  for i in range(n-1,-1,-1) : 
    print("  "*base + "* "*i)
  
def leftTree(n) :
  base = math.ceil(n / 2)
  for i in range(n) : 
    print("  "*(n-i) + "* "*i)
  print("* "*(base + n))
  for i in range(n-1,-1,-1) : 
    print("  "*(n-i) + "* "*i)

# ทำต้นไม่เอียงซ้าย ขวา คว่ำ
normalTree(n)
print("---------------------------------------")
downTree(n)
print("---------------------------------------")
rightTree(n)
print("---------------------------------------")
leftTree(n)