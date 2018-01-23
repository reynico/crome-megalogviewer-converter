import Tkinter,tkFileDialog
import csv
import os

root = Tkinter.Tk()
root.filename = tkFileDialog.askopenfilename(title = "Select file",filetypes = (("datalog files","*.csv"),("all files","*.*")))

# Remove double quotes
writer = csv.writer(open(os.path.dirname(root.filename)+"/edited-"+os.path.basename(root.filename), "wb"), quoting=csv.QUOTE_NONE)
reader = csv.reader(open((root.filename), "rb"), skipinitialspace=True)
reader.next()
writer.writerow(["Time","Engine Speed (RPM)","Vehicle Speed (Kmh)","Gear","Manifold Pressure (mbar)","Boost (psi)","Throttle Position (%)","Injector Duration (ms)","Duty Cycle (%)","Ignition Advance","Knock Retard","Air Temperature (C)","Coolant Temperature (C)","O2 Voltage","Lambda","Air Fuel Ratio","VTEC","CEL"])
flag=1
for row in reader:
	# Speed Mph to Kmh
	row[2] = str(round((float(row[2]) * 1.6),2))
	# Air temp F to C
	row[11] = str(round((float(row[11]) - 32)  / 9.0 * 5.0,2))
	# Coolant temp F to C
	row[12] = str(round((float(row[12]) - 32)  / 9.0 * 5.0,2))
	# VTEC On/Off to 0/1
	if row[16] == 'OFF':
		row[16] = '0'
	else:
		row[16] = '1'
	writer.writerow(row)