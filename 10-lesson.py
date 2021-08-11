#son = 1 
#while son <=31:
#	print(son)
#	son = son + 1

from random import randint

kodlar = [333, 334]
yangi_kod = randint(332, 334)

i = 0

while yangi_kod in kodlar:

	i +=1
	yangi_kod = randint(332, 334)
	
print('Takrorlanish soni: ', i)
print(yangi_kod) 