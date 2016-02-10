import time
import wunderground
from wunderground import *

weather = Conditions("4d2429c206187a02","emeryville","ca")
forecast = Forecast("4d2429c206187a02","emeryville","ca")
weatheroutput1 = ("WX: " + str(weather.condition()) + " " + str(weather.temperature_fahrenheit()) + "F ")
#    print weatheroutput1
weatheroutput2 = ("WX: " + str(weather.wind_speed()).zfill(2) + "MPH       ")
#    print weatheroutput2
