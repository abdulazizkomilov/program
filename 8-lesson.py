# summa = input('Summani kiriting: ')

# if summa.isdigit() and int(summa) > 0 and int(summa) < 1000000:
#	print('Tashakkur :)')
# else:
#	print('Xatolik bor :(')

# ism = input('Ismingizni kiriting: ')
# familya = input('Familyangizni kiriting: ')

# if ism or familya:
#	print('Tashakkur :)')
# else: 
#	print('Ismingizni yoki Familyangizni kiriting: ')

son = input('1 dan 30 gacha bo`lgan sonlardan birini kiritting:  ')
if son.isdigit():
	son = int(son)
	if son > 0 and son < 30:
		qoldiq = son % 10
		letter = ''
		if son > 9 and son < 19:
			letter = 'O`n '
		elif son > 20 and son < 30:
			letter = 'Yigirma '
		if qoldiq == 1:
			letter += 'Bir'
		elif qoldiq == 2:
			letter += 'Ikki'
		elif qoldiq == 3:
			letter += 'Uch'
		elif qoldiq == 4:
			letter += 'To`rt'
		elif qoldiq == 5:
			letter += 'Besh'
		elif qoldiq == 6:
			letter += 'Olti'
		elif qoldiq == 7:
			letter += 'Yitti'
		elif qoldiq == 8:
			letter += 'Sakkiz'
		elif qoldiq == 9:
			letter += 'To`qqiz'

		print(letter)
	else:
		print('1 dan 30 gacha bo`lgan sonlardan birini kiritting:  ')
else:
	print('Son kiritting:  ')
