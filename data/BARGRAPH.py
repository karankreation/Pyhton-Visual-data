import matplotlib.pyplot as plt


labels = ['500M', '1000M', '1500M', '3000M', '5000M', '10000M']
men_means = [3, 6, 3, 0, 6, 8]
women_means = [1, 5, 5, 4, 3, 0]
width = 0.35      

fig, ax = plt.subplots()

ax.bar(labels, men_means, width, label='Men')
ax.bar(labels, women_means, width, bottom=men_means,
       label='Women')

ax.set_ylabel('Medals')
ax.set_title('Gold Medals under 50km races after year 2000- AUSTRALIA')
ax.legend()

plt.show()