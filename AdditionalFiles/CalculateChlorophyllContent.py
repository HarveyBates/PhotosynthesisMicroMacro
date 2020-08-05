import csv
import pandas as pd
import os
import numpy as np

directory_of_file = "C:\\Users\\Owner\\OneDrive - UTS\\Chapter 4\\Chapter 4 Experimental Data\\Chlorophyll Extraction\\Day3(New_Spectrometer).xlsx"

directory_of_output = "C:\\Users\\Owner\\OneDrive - UTS\\Chapter 4\\Chapter 4 Experimental Data\\Organised Data\\Chlorophyll_content.csv"

Day_Number = 3
Methanol_Volume = 1
Culture_Volume = 3

data = pd.read_excel(directory_of_file)

# print(data["Wavelength"][1361]) #666
# print(data["Wavelength"][1322]) #653
# print(data["Wavelength"][793]) #470
with open(directory_of_output, "w", newline="") as f:
	writer = csv.writer(f)
	writer.writerow(["PB#", "Chl_a", "Chl_b", "Carotenoids", "Day Number"])
	for i in range(1, 11):
		if i != 5:
			# ## Equations Using Methanol ##
			Tran_666 = data["PB{}".format(i)][1361]
			Tran_653 = data["PB{}".format(i)][1322]
			Tran_470 = data["PB{}".format(i)][793]

			Abs_666 = -np.log10(Tran_666/100)
			Abs_653 = -np.log10(Tran_653/100)
			Abs_470 = -np.log10(Tran_470/100)

			## Units: mg / L ##
			Chl_a = (((15.65 * Abs_666) - (7.340 * Abs_653)) * Methanol_Volume) / Culture_Volume
			Chl_b = (((27.05 * Abs_653) - (11.21 * Abs_666)) * Methanol_Volume) / Culture_Volume
			Carotenoids = ((1000 * Abs_470) - (2.860 * Chl_a) - (129.2 * Chl_b)) / 245

			print(Chl_a, Chl_b, Carotenoids)


			writer.writerow(["PB{}".format(i), Chl_a, Chl_b, Carotenoids, Day_Number])




