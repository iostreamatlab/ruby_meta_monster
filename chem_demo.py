# coding=utf-8

# 计算化学式及化学式质量

from chempy import Substance
ferricyanide = Substance.from_formula('Fe(CN)6-3')
ferricyanide.composition == {0: -3, 26: 1, 6: 6, 7: 6}  # 0 for charge

print(ferricyanide.unicode_name)
print(ferricyanide.latex_name + ", " + ferricyanide.html_name)
print('%.3f' % ferricyanide.mass)


# 测量PH值

from collections import defaultdict
from chempy.equilibria import EqSystem
eqsys = EqSystem.from_string("""HCO3- = H+ + CO3-2; 10**-10.3
H2CO3 = H+ + HCO3-; 10**-6.3
H2O = H+ + OH-; 10**-14/55.4
""")
arr, info, sane = eqsys.root(defaultdict(float, {'H2O': 55.4, 'HCO3-': 1e-2}))
conc = dict(zip(eqsys.substances, arr))
from math import log10
print("pH: %.2f" % -log10(conc['H+']))


# 测量离子浓度

from chempy import ReactionSystem  # The rate constants below are arbitrary
rsys = ReactionSystem.from_string("""2 Fe+2 + H2O2 -> 2 Fe+3 + 2 OH-; 42
	   2 Fe+3 + H2O2 -> 2 Fe+2 + O2 + 2 H+; 17
       H+ + OH- -> H2O; 1e10
       H2O -> H+ + OH-; 1e-4""")  # "[H2O]" = 1.0 (actually 55.4 at RT)
from chempy.kinetics.ode import get_odesys
odesys, extra = get_odesys(rsys)
from collections import defaultdict
import numpy as np
tout = sorted(np.concatenate((np.linspace(0, 23), np.logspace(-8, 1))))
c0 = defaultdict(float, {'Fe+2': 0.05, 'H2O2': 0.1, 'H2O': 1.0, 'H+': 1e-2, 'OH-': 1e-12})
result = odesys.integrate(tout, c0, atol=1e-12, rtol=1e-14)
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
for ax in axes:
 _ = result.plot(names=[k for k in rsys.substances if k != 'H2O'], ax=ax)
 _ = ax.legend(loc='best', prop={'size': 9})
 _ = ax.set_xlabel('Time')
 _ = ax.set_ylabel('Concentration')
 _ = axes[1].set_ylim([1e-13, 1e-1])
 _ = axes[1].set_xscale('log')
 _ = axes[1].set_yscale('log')
 _ = fig.tight_layout()

plt.show()