import matplotlib.pyplot as plt

rows = 5
plt.figure(figsize=(6, 6))
for i in range(rows):
    for j in range(rows - i - 1, rows + i):
        plt.scatter(j, i, s=800, c='purple')
for i in range(rows - 2, -1, -1):
    for j in range(rows - i - 1, rows + i):
        plt.scatter(j, -(2 * rows - i - 2), s=800, c='purple')

plt.xlim(-0.5, 2 * rows - 1.5)
plt.ylim(-2 * rows + 1.5, 0.5)
plt.axis('off')

plt.gca().set_aspect('equal', adjustable='datalim')
plt.title("Diamond Pattern Plot", fontsize=14)

plt.show()