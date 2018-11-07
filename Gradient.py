x0 = 0
y0 = 0
d = 0.01
precision = 0.00001
lastx_step = 1
lasty_step = 1
iterations = 100
counter = 0

df = lambda x, y: 1 / 2 * x ** 2 + 1 / 3 * y ** 2 - x*y/4

while (lastx_step > precision) and (lasty_step > precision) and (counter < iterations):
    prev_x = x0
    prev_y = y0
    x0 -= d * df(x0,y0)
    y0 -= d * df(x0,y0)
    lastx_step = abs(x0-prev_x)
    lasty_step = abs(y0-prev_y)
    counter += 1

print(df(x0,y0))