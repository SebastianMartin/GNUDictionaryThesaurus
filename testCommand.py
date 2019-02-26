import os
import time
total = 0
for i in range(5):
	s = os.popen('sensors').readlines()
	temp = float(s[11][16:20])
	total += temp
	print(temp)
	time.sleep(5)
print(total/5)