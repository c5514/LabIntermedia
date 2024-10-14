import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def magnetic(z, a): #a es la razón entre la distancia entre las espiras y el radio de estas
    return 4/(10**7)*np.pi*1.421*154/(2*19.05)*(1/((1+(z/19.05+a/2)**2)**1.5) + 1/((1+(z/19.05-a/2)**2)**1.5))*100000

z = np.linspace(-30,30,200)

file_path = "./Datos.xlsx"
data = pd.read_excel(file_path, sheet_name="a=R", usecols=[0,1,2,3], skiprows=1, nrows=2459)
X1axis = data.iloc[:, 0].values
Y1axis = data.iloc[:, 1].values
dX1 = data.iloc[:, 2].values
dY1 = data.iloc[:, 3].values

data2 = pd.read_excel(file_path, sheet_name="a=0.5 R", usecols=[0,1,2,3], skiprows=1, nrows=2459)
X2axis = data2.iloc[:, 0].values
Y2axis = data2.iloc[:, 1].values
dX2 = data2.iloc[:, 2].values
dY2 = data2.iloc[:, 3].values

data3 = pd.read_excel(file_path, sheet_name="a=2R", usecols=[0,1,2,3], skiprows=1, nrows=2459)
X3axis = data3.iloc[:, 0].values
Y3axis = data3.iloc[:, 1].values
dX3 = data3.iloc[:, 2].values
dY3 = data3.iloc[:, 3].values

plt.errorbar(X1axis, Y1axis, xerr=dX1, yerr=dY1, fmt='.', capsize=2,color='blue')
plt.plot(z,magnetic(z,1),color='gray',label='Curva teórica')

plt.errorbar(X2axis, Y2axis, xerr=dX2, yerr=dY2, fmt='.', capsize=2,color='blue')
plt.plot(z,magnetic(z,0.5),color='gray',label='Curva teórica')

plt.errorbar(X3axis, Y3axis, xerr=dX3, yerr=dY3, fmt='.', capsize=2,color='blue')
plt.plot(z,magnetic(z,2),color='gray',label='Curva teórica')

plt.xlabel(r'$z$ (cm)')
plt.ylabel(r'$B$ (mT)')
plt.title(r'$B$ vs $z$')
plt.legend()
plt.grid(True)
plt.show()

