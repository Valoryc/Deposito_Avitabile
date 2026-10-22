import matplotlib.pyplot as plt #libreria base

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure()
plt.plot(x, y)

# aggiunge bellezza al grafico
plt.title('Grafico a Linee')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()