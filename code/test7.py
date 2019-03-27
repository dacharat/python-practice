# def f(name="No") :
#   print(f'Hello,{name}')

# f('Jack')
# f()

# def f(a,b,c,d):
#   print(a,b,c,d)
#   return (a + b) * (c - d)

# print(f(4,d=1,c=2,b=3))

# l = list(range(1,6))
# l = [i*i for i in range(1,6)]
# l1 = [0,1,2]
# l2 = [3,4,5]
# print(l1+l2)

# l = [1,3,5,...,49]
# l = [ i for i in range(1,51,2)]
# l = [ i for i in range(1,50) if i % 2 ==1]
# l = [i if i % 2 == 1 else 0 for i in range(1,50)]
# print(l)
# l = list(range(1,51,2))

# l = ["a","b","c"]
# '''
# l.append("d") # l += ["d"]
# item = l.pop()
# print(item)
# print(l)
# '''
# if "d" in l : print(True)
# else : print(False)

# if "a" not in l : 
#   print(-1)
# else :
#   print(l.index("a"))

# l = ["a","b","c","d","e","f"]
# print(l[-2]) #"c"
# print(l[1:])
# print(l[:])
# print(l[:5])
# print(l[::2])
# print(l[::-1])
# print(len(l))
# for i in l : 
#   print(i)
# print(":".join(l)) # item in list must be string

# l = [1,2,3,4,5]
# print(sum(l), min(l), max(l), sum(l)/len(l))
# print(":".join([str(i) for i in l]))
# print(min(["hell","hello","ho"]))

# text = input("Enter string: ")
# def count(text) : 
#   return len([i for i in text.lower() if i in 'aeiou'])
#   # x = 0
#   # for i in text.lower() :
#   #   if(i in 'aeiou'): 
#   #     x+=1
#   # return x
# print(f'There is/are {count(text)} vowel(s)')

# word = 'abcdefc'
# print(word[::-1])
# print(word.find("g"))
# print(word.replace("c","g"))

# l = [[1,2,3], [4,5]]
# print(l[1][0])

from pprint import pprint
# row=5
# col=6
# matrix=[[0 for j in range(col)] for i in range(row)]
# # matrix=[]
# # for i in range(row): 
# #   cur_row = [0 for j in range(col)]
# #   matrix.append(cur_row)
# pprint(matrix)

# a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# b = [[16,15,14,13],[12,11,10,9],[8,7,6,5],[4,3,2,1]]
# # a+b, a=b, at, ca, at, a*b
# def sumMatrix(a,b): 
#   return [[a[i][j]+b[i][j] for j in range(len(a[0]))]  for i in range(len(a)) ]
# print(sumMatrix(a,b))
# def mul(a,c) :
#   return [[a[i][j]*c for j in range(len(a[0]))] for i in range(len(a)) ]
# def t(a):
#   return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

# d = {'a': 1, 'b': 2, 'c': 3}
# print(type(d))
# for i in d: 
#   print(i,d[i])
# print(list(d.keys()))
# print(list(d.values()))
# d['d'] = 4
# print(d)
# d['e'] = [1,2,3,4]
# print(d)
# print(d['e'][2])
# d['f'] = {'j': 1, 'k': 2}
# print(d['f']['j'])
# d.setdefault('g',[])
# d.setdefault('g','')
# print(d)
# del d['a']
# del d['f']['j']
# print(d)
# print(d.get('b'))
# print(d.get('a'))
# # print(d['a']) # Error
# d.update(d['f'])
# print(d)
# d['k'] = 3
# print(d)

# l = [3,5,2,4,1]
# print(sorted(l, reverse=True))
# l.sort()

# a = [1,2,3,4]
# def f(a): 
#   a[0] = 5
#   print(a)
# f(a)
# print(a)

f = open('test1.py', 'r')
# a = f.readlines()
# print(a)

# a = f.read().split('\n')
# line = f.readline()
# while line != '' :
#   print(line)
#   line = f.readline()

for line in f: 
  print(line)