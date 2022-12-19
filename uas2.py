import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Grafik karyawan yang resain perbulan

subjects = ['maret', 'april', 'mei', 'juni', 'juli']
y = [20, 11, 8, 12, 6]
x = [22, 54, 30, 20, 11]

plt.plot(subjects, y, color='green',marker='o', label='My Marks')
plt.title("Grafik karyawan yang resain perbulan")
plt.xlabel("BULAN")
plt.ylabel("JUMLAH YANG RESAIN")
plt.grid()
plt.show()