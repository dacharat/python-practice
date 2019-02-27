# หาจำนวนเฉพาะ
number = 0
for i in range(2,101) : 
  num = 0
  for y in range(1,i+1) :
    if i%y == 0 :
      num+=1
  if num == 2 :
    number+= 1
    print(i, end=" ")
  # print("num: " + str(num))

print("\n" + str(number))