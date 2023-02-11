import matplotlib.pyplot as plt
import squarify

labels = ["A", "B", "C", "D","E", "F", "G", "H", "I"]
sizes = [100, 75, 50, 25, 20, 10, 5, 2, 1]

fig, ax = plt.subplots()
squarify.plot(sizes=sizes, label=labels, ax=ax)
plt.show()

