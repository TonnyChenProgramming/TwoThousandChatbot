import matplotlib.pyplot as plt
def repeat(x):
    y = 2 * x*x -1
    return y
x1_val = 0.2468
x1 = []
y1 = []
x2_val = 0.2469
x2 = []
y2 = []
for counter in range(0,100):
    x1.append(x1_val)
    x2.append(x2_val)
    x1_val = repeat(x1_val)
    x2_val = repeat(x2_val)
    y1.append(x1_val)
    y2.append(x2_val)
    plt.plot(x1,y1,'rs-')
    plt.plot(x2,y2,'bv-')
    plt.show()
print(f'x1:{x1_val}, x2:{x2_val}')

#0.2469      y:0.13918042201090408
#0.2468      y:-0.6391467869751952     