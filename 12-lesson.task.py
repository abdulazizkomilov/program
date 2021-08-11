import pygal
a = input('Iltimos tarmoq nomini kiriting: ')
a1 = (print(a),input('ning 3 ta qiymatini kiriting: '))
b = input('Iltimos tarmoq nomini kiriting: ')
b1 = (print(b),input('ning 3 ta qiymatini kiriting: '))
c = input('Iltimos tarmoq nomini kiriting: ')
c1 = (print(c),input('ning 3 ta qiymatini kiriting: '))

line_chart = pygal.Line()
line_chart.title = 'Statistika'
line_chart.x_labels = ['Fevral', 'Mart', 'Aprel', 'May']
line_chart.add(a, [a1])
line_chart.add(b, [b1])
line_chart.add(c, [c1])
line_chart.render_in_browser()