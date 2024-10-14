import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.core.dtypes.dtypes import np
from scipy.optimize import curve_fit

def linear(x, m, c):
    return m * x + c

file_path = "./Datos.xlsx"
data = pd.read_excel(file_path, sheet_name="K", usecols=[0,1,2,3], skiprows=1, nrows=2459)
Xaxis = data.iloc[:, 0].values
Yaxis = data.iloc[:, 1].values
dX = data.iloc[:, 2].values
dY = data.iloc[:, 3].values

fit, cov = curve_fit(linear, Xaxis, Yaxis, sigma=dY, absolute_sigma=True)

K = fit[0]
intercept = fit[1]
dK = np.sqrt(cov[0][0])
errIntercept = np.sqrt(cov[0][0])

print("K=",K,"+-",dK,"mT/A")

plt.errorbar(Xaxis, Yaxis, xerr=dX, yerr=dY, fmt='.', capsize=2,color='blue')
plt.plot(Xaxis,linear(Xaxis,K,intercept),color='gray',label="Ajuste de curva")

plt.xlabel(r'$I$ (cm)')
plt.ylabel(r'$B_H$ (mT)')
plt.title(r'$B_H$ vs $I$')
plt.legend()
plt.grid(True)
plt.show()

data2 = pd.read_excel(file_path, sheet_name="Horizontal",usecols=[0,1,2,3,4,5],skiprows=1,nrows=50)
alpH = data2.iloc[:, 1].values
dalpH = data2.iloc[:, 4].values
fieldH = data2.iloc[:, 0].values
dfieldH = data2.iloc[:, 3].values
Ih = data2.iloc[:, 2].values
dIh = data2.iloc[:, 5].values
YH = Ih*K
dYH = np.sqrt((dIh*K)**2+(dK*Ih)**2)
sinH = np.sin(alpH*np.pi/180)
cosH = np.abs(np.cos(alpH*np.pi/180))
XH = sinH/cosH

fit2, cov2 = curve_fit(linear, XH, YH)
Bh = fit2[0]
intercept2 = fit2[1]
dBh = np.sqrt(cov2[0][0])
errIntercept2 = np.sqrt(cov2[0][0])

print("Bh=",Bh,"+-",dBh,"mT")

plt.errorbar(XH, YH, yerr=dYH, fmt='.', capsize=2,color='blue')
plt.plot(XH,linear(XH,Bh,intercept2),color='gray',label="Ajuste de curva")
plt.xlabel(r'$\frac{\sin \alpha}{\sin(\Phi-\alpha)}$')
plt.ylabel(r'$IK$ (mT)')
# plt.title(r'$B_H$ vs $I$')
plt.legend()
plt.grid(True)
plt.show()

