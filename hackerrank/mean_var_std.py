import numpy as np

matrix = []
n, m = input().split()

for i in range(int(n)):
  val = list(map(int, input().split()))
  matrix.append(val)

print(np.mean(matrix, axis=1))
print(np.var(matrix, axis=0))
print("{:.11f}".format(np.std(matrix, axis=None )), end="\n")