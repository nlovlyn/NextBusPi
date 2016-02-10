import lcddriver
from time import *
import time
from predict import predict
import threading
import weather
from weather import *

lcd = lcddriver.lcd()
boot = 0

# List of bus lines/stops to predict.  Use routefinder.py to look up
# lines/stops for your location, copy & paste results here.  The 4th
# element on each line can then be edited for brevity if desired.
stops = [
  ( 'emery', 'Hollis', 'ho65_o', 'EMY' ),
  ( 'emery', 'Hollis', '65ho_i', 'BART' ),
  ( 'emery', 'powell', '65sh_o', 'BART' ),
  ( 'actransit', 'J', '0601170', 'SF' ),
#  ( 'actransit', '802', '1018390', 'SF' ),
  ( 'actransit', 'F', '0601160', 'SF' ),
]

# Populate a list of predict objects from stops[].  Each then handles
# its own periodic NextBus server queries.  Can then read or extrapolate
# arrival times from each object's predictions[] list (see code later).
predictList = []
for s in stops:
	predictList.append(predict(s))
while boot < 3:

	boottime = str(10 - boot)
	lcd.lcd_display_string("Loading data", 1)
	lcd.lcd_display_string("Please wait...", 2)
	lcd.lcd_display_string("ETA: " + boottime.zfill(2) + " sec", 3)
	time.sleep(1) # Allow a moment for initial results
	boot = boot + 1

	
lcd.lcd_clear()
lcd.lcd_display_string(weatheroutput1, 1)


# Define stops
HollisEMY = predictList[0].data[1]
HollisBART = predictList[1].data[1]
Powell = predictList[2].data[1]
J = predictList[3].data[1]
F = predictList[4].data[1]

# Define predictions1
HE0 = 0
HE0S = 0
HE1 = 0
HE1S = 0
OutputHE = 0

HB0 = 0
HB0S = 0
HB1 = 0
HB1S = 0
OutputHB = 0

P0 = 0
P0S = 0
P1 = 0
P1S = 0
OutputP = 0

J0 = 0
J0S = 0
J1 = 0
J1S = 0
OutputJ = 0

F0 = 0
F0S = 0
F1 = 0
F1S = 0
OutputF = 0
weatherloop = 0
loopcount = 0
while True:
	currentTime = time.time()
	# wait for array to be filled before attempting to access

#	if weatherloop > 2:
#		lcd.lcd_display_string(weatheroutput, 1)
#		weatherloop = 0
#		print weatheroutput

	weatherloop = weatherloop +1
	if len(predictList) > 0 and predictList[0].predictions:
		HE0S = predictList[0].predictions[0]
		HE0 = HE0S / 60
		
#		if pl.predictions: # List of arrival times, in seconds
#					
		if len(predictList[0].predictions) > 2:
			HE1S = predictList[0].predictions[1]
			HE1 = HE1S / 60
		else:
			HE1 = "ND"
		#HE1S = predictList[0].predictions[1]
		#HE1 = HE1S / 60
		h1 = str(HollisEMY)
		h2 = str(HE0)
		h3 = str(HE1)
		OutputHE = h1 + " >EMY:  " + h2.zfill(2) + ", " + h3.zfill(2)
	else:
		OutputHE = HollisEMY + " >EMY: No Data"

	if len(predictList) > 0 and predictList[1].predictions:
		HB0S = predictList[1].predictions[0]
		HB0 = HB0S / 60
		
		if len(predictList[1].predictions) > 2:
			HB1S = predictList[1].predictions[1]
			HB1 = HB1S / 60
		
		else:
			HB1 = "ND"

		B1 = str(HollisBART)
		B2 = str(HB0)
		B3 = str(HB1)
		OutputHB = B1 + " >BART: " + B2.zfill(2) + ", " + B3.zfill(2)
	else:
		OutputHB = HollisBART + " >BART:No Data"

	if len(predictList) > 0 and predictList[2].predictions:
		P0S = predictList[2].predictions[0]
		P0 = P0S / 60
		if len(predictList[2].predictions) > 2:
			P1S = predictList[2].predictions[1]
			P1 = P1S / 60
		
		else:
			P1 = "ND"


		P11 = str(Powell)
		P12 = str(P0)
		P13 = str(P1)
		OutputP = "Powell >BART: " + P12.zfill(2) + ", " + P13.zfill(2)
	else:
		OutputP = "Powell >BART:No Data"

	if len(predictList) > 0 and predictList[3].predictions:
		J0S = predictList[3].predictions[0]
		J0 = J0S / 60
		if len(predictList[3].predictions) > 2:
			J1S = predictList[3].predictions[1]
			J1 = J1S / 60
		
		else:
			J1 = "ND"


		J11 = str(J)
		J12 = str(J0)
		J13 = str(J1)
		OutputJ = J11 + " >SF: " + J12.zfill(2) + ", " + J13.zfill(2)
	else:
		OutputJ = J + " >SF:No Data"

	if len(predictList) > 0 and predictList[4].predictions:
		F0S = predictList[4].predictions[0]
		F0 = F0S / 60
		if len(predictList[4].predictions) > 2:
			F1S = predictList[4].predictions[1]
			F1 = F1S / 60
		
		else:
			HF1 = "ND"

		f11 = str(F)
		f12 = str(F0)
		f13 = str(F1)
		OutputF = f11 + " >SF: " + f12.zfill(2) + ", " + f13.zfill(2)
	else:
		OutputF = F + " >SF:No Data"
	loopcount = loopcount + 1
	if loopcount > 5:
		loopcount = 0
		lcd.lcd_clear()
	if (loopcount % 2 == 0):
		lcd.lcd_display_string(weatheroutput1, 1)
		lcd.lcd_display_string(OutputHE, 2)
		lcd.lcd_display_string(OutputF, 4)
	else:
		lcd.lcd_display_string(weatheroutput2, 1)
		lcd.lcd_display_string(OutputHB, 2)
		lcd.lcd_display_string(OutputJ, 4)
		
	lcd.lcd_display_string(OutputP, 3)
	print OutputHE
	print OutputHB
	print OutputP
	print OutputJ
	print OutputF

	#lcd - first line
	# 
	#for pl in predictList:
		#time.sleep(.2)
		#print pl.data[1] + ' ' + pl.data[3] + ':'
		#print pl.data[3]
		#lcd.lcd_display_string(pl.data[3], 4)
		#if pl.predictions: # List of arrival times, in seconds
					#for p in pl.predictions:
						# Extrapolate from predicted arrival time,
						# current time and time of last query,
						# display in whole minutes.
						#t = p - (currentTime - pl.lastQueryTime)
						#print '\t' + str(int(t/60)) + ' min'
						#lcd.lcd_display_string(t, 4)
		#else:
					#print '\tNo predictions'
					#lcd.lcd_display_string("No predictions", 4)
					#prevTime = currentTime;
	time.sleep(5) # Refresh every ~5 seconds

