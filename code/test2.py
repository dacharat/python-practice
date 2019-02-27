# หาค่าจากการ input t ที่ค่าต่างกัน
t = int(input("t: "))
result = 0
if t <= 10:
  result = (4 ** t)/100
elif t <= 20:
  result = 1100 - 5(t)
elif t <= 30:
  result = 11 * t ** 3
else: 
  result = 0

print(f"v({t}): {result:.3f}")