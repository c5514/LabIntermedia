import pandas as pd
import matplotlib.pyplot as plt

file_path = "./Datos.xlsx"
data = pd.read_excel(file_path, sheet_name="100 mm", usecols=[0,1,2,3], skiprows=1, nrows=2459)
X1axis = data.iloc[:, 0].values
Y1axis = data.iloc[:, 1].values
dX1 = data.iloc[:, 2].values
dY1 = data.iloc[:, 3].values

data2 = pd.read_excel(file_path, sheet_name="140 mm", usecols=[0,1,2,3], skiprows=1, nrows=2459)
X2axis = data2.iloc[:, 0].values
Y2axis = data2.iloc[:, 1].values
dX2 = data2.iloc[:, 2].values
dY2 = data2.iloc[:, 3].values

data3 = pd.read_excel(file_path, sheet_name="160 mm", usecols=[0,1,2,3], skiprows=1, nrows=2459)
X3axis = data3.iloc[:, 0].values
Y3axis = data3.iloc[:, 1].values
dX3 = data3.iloc[:, 2].values
dY3 = data3.iloc[:, 3].values

data4 = pd.read_excel(file_path, sheet_name="a=R", usecols=[0,1,2,3], skiprows=1, nrows=2459)
X4axis = data4.iloc[:, 0].values
Y4axis = data4.iloc[:, 1].values
dX4 = data4.iloc[:, 2].values
dY4 = data4.iloc[:, 3].values
mask = (X4axis >= 0) & (X4axis <= 19)
filtered_X = X4axis[mask]
filtered_Y = Y4axis[mask]
filtered_dX = dX4[mask]
filtered_dY = dY4[mask]

plt.errorbar(filtered_X, filtered_Y, xerr=filtered_dX, yerr=filtered_dY, fmt='.', capsize=2,color='gray',label='r = 0 mm')

plt.errorbar(X1axis, Y1axis, xerr=dX1, yerr=dY1, fmt='.', capsize=2,color='blue',label = 'r= 100 mm')

plt.errorbar(X2axis, Y2axis, xerr=dX2, yerr=dY2, fmt='.', capsize=2,color='green', label='r = 140 mm')

plt.errorbar(X3axis, Y3axis, xerr=dX3, yerr=dY3, fmt='.', capsize=2,color='red',label='r= 160 mm')



plt.xlabel(r'$z$ (cm)')
plt.ylabel(r'$B_z$ (mT)')
plt.title(r'$B_z$ vs $z$')
plt.legend()
plt.grid(True)
plt.show()

