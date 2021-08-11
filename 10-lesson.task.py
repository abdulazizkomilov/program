son = input('Butun son kiriting: ')
#if a.isdigit():
#	else:
#	print('Xatolik!!!')
while not son.isdigit():
	print('Xatolik!!!')
	son = input('Iltimos butun son kiriting: ')
	if son.isdigit():
		print('Raxmat!')
	