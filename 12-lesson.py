# son = 45
# print('son = ', son)
# sonlar = [23, 34, 234, -22, 'sds', 'wh']
# print('sonlar = ', sonlar)

# sonlar = [12, 223, 'sds', -33]
# print(len(sonlar))
# sonlar.append('php')
# print(sonlar)

import pygal

line_chart = pygal.Line()
line_chart.title = 'Statistika'
line_chart.x_labels = ['Fevral', 'Mart', 'Aprel', 'May']
line_chart.add('Facebook', [9.24, 13.7, 16.24, 18.07])
line_chart.add('Instagram', [24.03, 26.81, 21.03, 22.77])
line_chart.add('Youtube', [8.95, 15.81, 19.19, 22.67])
line_chart.render_in_browser()
