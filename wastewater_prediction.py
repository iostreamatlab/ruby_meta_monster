# coding:utf-8 
from __future__ import print_function
import numpy as np
import statsmodels.api as sm
nsample = 50
sig = 0.5
x1 = np.linspace(0, 20, nsample)
X = np.column_stack((x1, np.sin(x1), (x1+3)**2))
X = sm.add_constant(X)
beta = [4., 0.5, 0.07, -0.02]
y_true = np.dot(X, beta)+1200
y = y_true + sig * np.random.normal(size=nsample)
olsmod = sm.OLS(y, X)
olsres = olsmod.fit()
ypred = olsres.predict(X)
x1n = np.linspace(20.5,25, 10)
Xnew = np.column_stack((x1n, np.sin(x1n), (x1n+3)**2))
Xnew = sm.add_constant(Xnew)
ynewpred =  olsres.predict(Xnew) # predict out of sample
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(x1, y, 'o', label="DATA")
ax.plot(x1, y_true, 'b-', label="TRUE")
ax.plot(np.hstack((x1, x1n)), np.hstack((ypred, ynewpred)), 'r', label="OLS predict")
ax.legend(loc="best");
ax.set_title('Oil type',fontsize=12,color='k')
plt.show()



'''
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[3,6,7,9,2]
 
fig,ax=plt.subplots(1,1)
ax.plot(x,y,label='trend')
ax.set_title('title test',fontsize=12,color='r')
plt.show()

'''





