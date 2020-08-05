import csv 
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("C:\\Users\\Owner\\OneDrive - UTS\\Chapter 4\\Chapter 4 Experimental Data\\Sigma(II)\\Day3 R1")

with open ("C:\\Users\\Owner\\OneDrive - UTS\\Chapter 4\\Chapter 4 Experimental Data\\Organised Data\\Sigma_values.csv", "a", newline="") as f:
	writer = csv.writer(f)

	for i in range(1, 11):
		
		if i != 5 and i != 0:

			filename = "PB{}".format(i) + ".csv"
			print(filename)
			data = pd.read_csv(str(filename), sep=';')
			print(data.head())

			sigma = data.iloc[1:6, 12:13]
			print(sigma.head())
			print(sigma["Sigma"][2])
			writer.writerows([sigma["Sigma"]])
		
		else:
			pass

f.close()