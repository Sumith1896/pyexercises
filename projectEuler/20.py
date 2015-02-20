import sys
import os

def fact(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n*fact(n-1)

ans = fact(100)
digits = str(ans)

x = 0
for i in range(len(digits)):
	x = x + int(digits[i])

print x