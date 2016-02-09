import lcddriver
import time
from predict import predict
import threading

lcd = lcddriver.lcd()

# List of bus lines/stops to predict.  Use routefinder.py to look up
# lines/stops for your location, copy & paste results here.  The 4th
# element on each line can then be edited for brevity if desired.
stops = [
  ( 'emery', 'Hollis', 'ho65_o', 'EMY' ),
  ( 'emery', 'Hollis', '65ho_i', 'BART' ),
  ( 'emery', 'powell', '65sh_o', 'BART' ),
  ( 'actransit', 'J', '0600190', 'SF' ),
  ( 'actransit', 'F', '0601160', 'SF' ),
]

# Populate a list of predict objects from stops[].  Each then handles
# its own periodic NextBus server queries.  Can then read or extrapolate
# arrival times from each object's predictions[] list (see code later).
predictList = []
for s in stops:
	predictList.append(predict(s))

time.sleep(1) # Allow a moment for initial results

# Define stops
HollisEMY = predictList[0].data[1]
HollisBART = predictList[1].data[1]
Powell = predictList[2].data[1]
J = predictList[3].data[1]
F = predictList[4].data[1]

# Define predictions1
HEP0 = 0
HE0S = 0
HEP1 = 0
HE1S = 0
HBP0 = 0
HB0S = 0
HBP1 = 0
HB1S = 0
PP0 = 0
P0S = 0
PP1 = 0
P1S = 0
JP0 = 0
J0S = 0
JP1 = 0
J1S = 0
FP0 = 0
F0S = 0
FP1 = 0
F1S = 0

while True:
	currentTime = time.time()
	# wait for array to be filled before attempting to access
	if len(predictList) > 0 and predictList[0].predictions:
		print predictList[0].predictions[0]
		HE0S = predictList[0].predictions[0]
		
		
		lcd.lcd_display_string(b, 4)
	else:
		x = HollisEMY + ": No Data"
		lcd.lcd_display_string(x, 4)     

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
