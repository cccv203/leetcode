from sklearn.svm import SVR
import math
import numpy as np


u_k = np.zeros((500,1))
y_k = np.zeros((500))
# y_k[1] = 1

for i in range(u_k.shape[0]):
    u_k[i] = 0.19*math.sin(2*math.pi*i/50) + 0.95*math.sin(2*math.pi*i/20)

for i in range(2,y_k.shape[0]):
    y_k[i] = u_k[i]**3 + 0.3*math.sin(u_k[i-1]) + 0.6*math.sin(u_k[i-2])


# u_k = (u_k - np.min(u_k))/np.max(u_k)

x_train = u_k#np.array(range(500)).reshape(-1,1)
# x_train = (x_train - np.min(x_train))/np.max(x_train)

clf = SVR(C=100,epsilon=0.001,gamma=20)
clf.fit(x_train,y_k[:500])
y_pre = clf.predict(x_train)
import matplotlib.pyplot as plt

plt.scatter(range(500),y_k[:500])
plt.plot(range(500),y_pre,'r')
plt.show()

plt.figure()
err = (y_k - y_pre)/y_k
plt.plot(range(500),err,'r')
plt.show()

