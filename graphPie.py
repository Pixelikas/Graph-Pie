import matplotlib.pyplot as plt

games = ['Zelda', 'Pokemon', 'The Last Of Us', 'God of War']
sell = [20, 40, 5, 35]

plt.title('Venda Franquias Jogos')

plt.pie(sell, labels = games)
plt.legend(games)

plt.show()