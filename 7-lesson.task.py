a = int(input('Yil kiriting: '))

if a%4!=0:
	print('Kabisa yil emas')
elif a%100==0:
	if a%400==0:
		print('Kabisa yil')
	else:
		print('Kabisa yil emas')
else:
	print('Kabisa yil')