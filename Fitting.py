from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

f = lambda x: x * np.sin(np.exp(.7*x))

a, b = 0, 4
npoints = 50
order = 13

xvalues = np.linspace(a,b,npoints)
yvalues = f(xvalues) + np.random.rand(npoints)-0.5

fit = np.polyfit(xvalues,yvalues,order,full=True)
yp = np.polyval(fit[0],xvalues)

plt.plot(xvalues, f(xvalues), label="Orignal Function")
plt.plot(xvalues, yvalues, 'o', label="Noise")
plt.plot(xvalues, yp, label="Polyfit " + str(order) + " sorder")

plt.xlabel('x')
plt.ylabel("$f(x)$")
plt.xlim([a,b])
plt.legend(fontsize=14)
plt.title("Noisy Fit")
plt.show()

"""
I found that using thte fucntion polynomial fit set
to the order of 13 produced the best estimation for my function.
I didn't think that it would need to be that big, but that's what works
"""