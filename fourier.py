import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("circular.txt",float)

l = np.fft.fft(data)

x = np.linspace(0.0,len(data), 501)

plt.plot(data)
plt.title("Unprocessed")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.savefig("first.png")
plt.show()

plt.plot(x,np.abs(l))
plt.title("Processed")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.savefig("second.png")
plt.show()


print("The orginal graph was 485 kBs")
print("The second file was 71 kBs")