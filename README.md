# NextBusPi
This code is designed to pull live data from NextBus and display it on a 4x20 LCD attached to the I2C pins on the GPIO.
It is capable of displaying two stops per line and two predictions per stop.
Currently working on adding current weather to be displayed.

Python front-end for the NextBus schedule service, for Raspberry Pi, etc.

routefinder.py: for selecting bus routes/stops for use with the other scripts. Crude textual interface is best used w/terminal with scroll-back ability. Only need to use this for setup, hence the very basic implementation.

predict.py: class that handles periodic queries to the NextBus server. Imported by other scripts; doesn't do anything on its own.

nextbus.py: Main scrypt. Prints NextBus data to a LCD.