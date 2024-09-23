# Plotting the data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelmin

file_path = "./LabIntermedia-Franck-Hertz/Mercurio/185-60-1,5-9/5.xlsx"
data = pd.read_excel(file_path, sheet_name=0, usecols="A:B", skiprows=1, nrows=2459)

voltages = data.iloc[:, 0].values
currents = data.iloc[:, 1].values

local_minima_indices = argrelmin(currents)[0]


minima_voltages = voltages[local_minima_indices]
minima_currents = currents[local_minima_indices]
strict_minima_indices = [i for i in local_minima_indices if currents[i] < currents[i-20] and currents[i] < currents[i+20]]

minima_voltages = voltages[strict_minima_indices]
minima_currents = currents[strict_minima_indices]

plt.plot(voltages, currents, label='Data')
plt.scatter(minima_voltages, minima_currents, color='red', label='Minima', zorder=5)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title('Franck-Hertz Experiment Data with Minima')
plt.legend()
plt.grid(True)
plt.show()


minima_data = pd.DataFrame({
    'Voltage (V)': minima_voltages,
    'Current (A)': minima_currents
})

minima_data.to_excel('./franck_hertz_minima.xlsx', index=False)
print("Minima data exported to 'franck_hertz_minima.xlsx'.")
