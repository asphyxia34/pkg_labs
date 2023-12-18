import matplotlib.pyplot as plt

with open("input_data.txt", "r") as file:
    data = [tuple(map(float, line.split())) for line in file]

omega, iterations = zip(*data)

plt.plot(omega, iterations, label='Data Points')
plt.title('Graph')
plt.xlabel('Omega')
plt.ylabel('Iterations')
plt.legend()
plt.show()
