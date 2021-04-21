import matplotlib.pyplot as plt


labels = ['GOLD-M', 'GOLD-W', 'SILVER-M', 'SILVER-W', 'BRONZE-M', 'BRONZE-W']
sizes = [1310, 611  , 1319, 611, 1315 , 604]



fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  

plt.show()