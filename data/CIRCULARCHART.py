# # of vancouver men with medal in ice hockey  - 95
# # of vancouver women with medal in ice hockey  - 40

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['Turin-M', 'Turin-W', 'Albertville-M', 'Albertville-W', 'Vancouver-M', 'Vancouver-W', 'Sochi-W', 'Sochi-M' ]
sizes = [19, 21, 0, 5, 23, 23, 25, 25 ]
explode = (0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.4, 0.4)


fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode,labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()