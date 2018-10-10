import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("circular.txt",float)

transform = np.abs(np.fft.fft2(data))



x = np.linspace(0.0,len(data), 501)

plt.imshow(data)
plt.title("Unprocessed")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.savefig("first.png")
plt.show()

plt.imshow(np.log(transform))
plt.title("Processed")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.savefig("second.png")
plt.show()

print(np.shape(data))
print(np.shape(transform))
