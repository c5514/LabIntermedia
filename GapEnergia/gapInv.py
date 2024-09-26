import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear_func(x, m, c):
    return m * x + c

file_path = "./Gap.xlsx"
# data = pd.read_excel(file_path, sheet_name="Germanio Inverse", usecols=[3,4,7,6], skiprows=1, nrows=2459)
# data = pd.read_excel(file_path, sheet_name="Germanio Inverse 2", usecols=[3,4,7,6], skiprows=1, nrows=2459)
# data = pd.read_excel(file_path, sheet_name="Silicio Inverse", usecols=[3,4,7,6], skiprows=1, nrows=2459)
data = pd.read_excel(file_path, sheet_name="Silicio Inverse 2", usecols=[3,4,7,6], skiprows=1, nrows=2459)
Yaxis = data.iloc[:, 0].values
Xaxis = data.iloc[:, 1].values

# dX = data.iloc[:, 2].values

dY = data.iloc[:, 3].values

fit, cov = curve_fit(linear_func, Xaxis, Yaxis, sigma=dY, absolute_sigma=True)

slope = fit[0]
intercept = fit[1]
errSlope = np.sqrt(cov[0][0])
errIntercept = np.sqrt(cov[1][1])

print("Slope:", slope)
print("Intercept:", intercept)
print("Error slope:", errSlope)
print("Error intercept:", errIntercept)

# plt.scatter(Xaxis, Yaxis, color='red', label='Puntos', zorder=5)
plt.plot(Xaxis, linear_func(Xaxis, slope, intercept), color='blue', label='Ajuste de curva')
plt.errorbar(Xaxis, Yaxis, yerr=dY, fmt='.', capsize=2)
plt.xlabel('1/T (1/K)')
plt.ylabel('ln(I0)')
# plt.title('Diodo de germanio invertido')
plt.title('Diodo de silicio invertido')
plt.legend()
plt.grid(True)
plt.show()
