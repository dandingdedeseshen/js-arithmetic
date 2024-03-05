def str_reverse(x):
  length = len(x)
  str = ''
  for i in range(length - 1, -1, -1):
    str += x[i]
  return str

def substr(x, y, z):
  return x[y:z]