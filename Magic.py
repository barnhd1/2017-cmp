import matplotlib.pyplot as plt

total = 100
m = 12
c = 1992
size = 11
x = 25
random_list = []

for i in range(total):      
    x = (m*x+c)%size - 5
    random_list.append(x)
plt.plot(random_list,".")
plt.show()