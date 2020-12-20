import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
x_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))
ax.bar(x_pos, performance, yerr=error, align='center',color='green', ecolor='black')
ax.set_xticks(x_pos)
ax.set_xticklabels(people)
ax.set_ylabel('Performance')
ax.set_title('How fast do you want to go today?')
plt.show()
