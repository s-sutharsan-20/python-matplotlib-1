import matplotlib.pyplot as plt
y1=[3,4,3,6,8]
x1=[1,2,3,4,5]
y2=[0,2,3,5,7]
x2=[1,2,3,4,5]
plt.plot(x1,y1,label='Line 1')
plt.plot(x2,y2,label='Line 2')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('LINE GRAPH')
plt.legend()
plt.show()
