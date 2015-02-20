c = 0

def prime(i):
	j =0
	for j in range(i):
		if(i%j==0):
			b = true

	return b
i = 600851475142
while i != 0:
	if 600851475143%i == 0 and  prime(i):
		break
	i=i -1

print i