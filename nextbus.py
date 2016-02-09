import lcddriver
import time
#from predict import predict
import predict
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

while True:
	currentTime = time.time()
	print predictList[0].data[1]
	print predictList[0].predictions[0]
	a = predictList[0].data[1]
	b =  predictList[0].predictions[0]
	lcd.lcd_display_string(a, 3)
	lcd.lcd_display_string(b, 4)
	#lcd - first line 
	for pl in predictList:
		time.sleep(.2)
		#print pl.data[1] + ' ' + pl.data[3] + ':'
		#print pl.data[3]
		#lcd.lcd_display_string(pl.data[3], 4)
		if pl.predictions: # List of arrival times, in seconds
					for p in pl.predictions:
						# Extrapolate from predicted arrival time,
						# current time and time of last query,
						# display in whole minutes.
						t = p - (currentTime - pl.lastQueryTime)
						#print '\t' + str(int(t/60)) + ' min'
						#lcd.lcd_display_string(t, 4)
		else:
					#print '\tNo predictions'
					#lcd.lcd_display_string("No predictions", 4)
					prevTime = currentTime;
	time.sleep(5) # Refresh every ~5 seconds
