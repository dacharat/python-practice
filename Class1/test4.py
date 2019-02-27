# หาครน. หรม.
a = int(input("a: "))
b = int(input("b: "))

# while a != b :
#   if a > b :
#     a = a-b
#   else :
#     b = b-a
# print("G.C.D = " + str(a))

answer = 1
for i in range(1,min(a,b) + 1) :
  if a % i == 0 and b % i == 0 :
    answer = i

print("G.C.D = " + str(answer))
print("L.C.D = " + str((a*b)//answer))

