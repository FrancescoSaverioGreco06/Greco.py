import matplotlib.pyplot as plt

data = {'carne': 21, 'pasta': 11, 'ortaggi': 15, 'frutta': 18}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('cosa preferiscono i giovani di oggi?')


plt.show()
