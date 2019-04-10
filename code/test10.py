# recusive

def fac(n):
  if n <= 1:
    return 1
  return n * fac(n-1)

print(fac(5))

# =======================================================

def fibo(n):
  if n <= 2:
    return 1
  return fibo(n-1) + fibo(n-2)

print(fibo(5))

# =======================================================

l = [fibo(i+1) for i in range(20)]

def binarySearch(n, l):
  if len(l) == 1 :
    return n == l[0]
  # mid_index = len(l)//2 ใช้แบบนี้ได้เหมือนกันแทน int(len(l)/2) -1
  if l[int(len(l)/2) -1] > n:
    return binarySearch(n, l[:int(len(l)/2) -1])
  return binarySearch(n, l[int(len(l)/2):])

print(binarySearch(350,l))
print(binarySearch(377,l))

# =======================================================

def isPrime(n, i = 2):
  if n == i:
    return True
  if n % i != 0:
    return isPrime(n, i+1)
  return False

print(isPrime(71))

# =======================================================
