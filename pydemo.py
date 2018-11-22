
import pykov


d = pykov.Matrix({('coal', 'WW'): 0.3483, ('coal', 'COD'): 0.2034,('coal', 'NHN'): 0.2658,
              ('oil',  'WW'): 0.1399, ('oil',  'COD'): 0.1820,('oil',  'NHN'): 0.2666,
              ('chemistry', 'WW'): 0.1397,('chemistry', 'COD'): 0.1826,('chemistry', 'NHN'): 0.1916,
              ('smelt', 'WW'): 0.0759, ('smelt', 'COD'): 0.0515, ('smelt', 'NHN'): 0.0417,
              ('farm', 'WW'): 0.0458,('farm', 'COD'): 0.1116,('farm', 'NHN'): 0.0355,})


T = pykov.Chain(d)

import matplotlib.pyplot as plt
import numpy as np

# create some data to use for the plot
dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000]/0.05)               # impulse response
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)]*dt  # colored noise

# the main axes is subplot(111) by default
plt.plot(t, s)
plt.axis([0, 1, 1.1*np.amin(s), 2*np.amax(s)])
plt.xlabel('time (s)')
plt.ylabel('current (nA)')
plt.title('Gaussian colored noise')



plt.show()

import statsmodels.api as sm
import statsmodels.formula.api as smf

# Load data
dat = sm.datasets.get_rdataset("Guerry", "HistData").data

# Fit regression model (using the natural log of one of the regressors)
results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=dat).fit()

# Inspect the results
print(results.summary())