import numpy as np
import sys

H = np.matrix([[0,1,1,1,1,0,0,1],[1,0,1,1,0,0,1,1],[0,1,1,0,1,1,1,1],[1,0,0,1,1,1,1,1]])
a = str(sys.argv[1])
f = open("./file.txt","w")
f.write(a)
for i in range(0, 4):
	x = 0
	for j in range(0,8):
		x = x + int(a[j]) * H[i,j]
	x = x%2
	f.write(str(x))
f.close()
