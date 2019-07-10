N = input()
array = []
list = []
for i in N:
  array.append(int(i))
array.append(int(array[0]))
for j in range(0,len(array) - 1):
  b = array[j] ** array[j + 1]
  list.append(b)
print(sum(list)
