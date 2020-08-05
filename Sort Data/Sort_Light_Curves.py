import csv 
import pandas as pd
import matplotlib.pyplot as plt
import os

dir_of_etr_data = "C:\\Users\\Owner\\OneDrive - UTS\\Chapter 4\\Chapter 4 Experimental Data\\Light Curves (MC-PAM)\\Day3 Rep1"
dir_of_sigma_data = "C:\\Users\\Owner\\OneDrive - UTS\\Chapter 4\\Chapter 4 Experimental Data\\Organised Data\\Sigma_values.csv"
dir_of_output_file = "C:\\Users\\Owner\\OneDrive - UTS\\Chapter 4\\Chapter 4 Experimental Data\\Organised Data\\Light_Curve_Values.csv"

os.chdir(dir_of_etr_data)

sigma_starting_point = 18
print(sigma_starting_point)
sigma = pd.read_csv(dir_of_sigma_data)

with open(dir_of_output_file, 'a', newline="") as f:
	writer = csv.writer(f)
	writer.writerow(["Date", "Time", "PAR", "Y(II)", "Y(NPQ)", "Y(NO)", 
		"NPQ", "qN", "qP", "qL", "ETR", "PAR(II)", "ETR(II)", "PB#" , "Sigma"])

	for p in range(1, 11):
		if p != 5:
			data = pd.read_csv("PB{}.csv".format(p), sep=";")
			Date = data["Date"]
			Time = data["Time"]
			PAR = data["PAR"]
			Y_II = data["Y(II)"]
			Y_NPQ = data["Y(NPQ)"]
			Y_NO = data["Y(NO)"]
			NPQ = data["NPQ"]
			qN = data["qN"]
			qP = data["qP"]
			qL = data["qL"]
			ETR = data["ETR"]

			
			PAR_II, ETR_II = [], []
			for x in range(len(PAR)):
				calc_par_II = sigma["625"][sigma_starting_point] * 0.6022 * PAR[x]
				PAR_II.append(calc_par_II)
				calc_etr_II = calc_par_II * (Y_II[x] / Y_II[3])
				ETR_II.append(calc_etr_II)

			for i in range(len(Date)):
				writer.writerow([Date[i], Time[i], PAR[i], Y_II[i], Y_NPQ[i], Y_NO[i],
				 NPQ[i], qN[i], qP[i], qL[i], ETR[i], PAR_II[i], ETR_II[i], "PB{}".format(p), 
				 sigma["625"][sigma_starting_point]])

			sigma_starting_point += 1

f.close()
