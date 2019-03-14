def filter_in_range(lst,low,high) :
  if len(lst) == 0:
    return []
  first = lst[0]
  lst.pop(0)
  if first > low and first < high : 
    return [first] + filter_in_range(lst,low,high)
  else :
    return filter_in_range(lst,low,high)
  return lst

print(filter_in_range([1,2,3,4,5],2,4))
print(filter_in_range([1,2,3,10,20,30,500,600,100,80,45], 15, 99))
# x = [1,2,3,4]
# x.pop(0)
# print(x)