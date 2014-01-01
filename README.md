analog-powermeter
=================

Python script to convert mouse movement data from a residential power meter to instantaneous kilowatt readings

This is my first time using python so forgive the crappiness

In order to monitor power usage in my home I needed to devise a way to read an analog dial.
A disassembled optical mouse can be used to measure the speed at which the dial is turning. This works through the glass of the dial as long as the mouse is disassembled and the light tube is removed. Sticky tape can then be used to hold the mouse PCB in place.

###Setup

There are several variables that need to be configured

* mFactor - This is a constant which depends on your mouse DPI and the diameter of your power meter's wheel. To determine mFactor you must get a direct mouse reading for one revolution.
* revkwh - This is usually listed on the power meter itself mine is 266.67 revolutions / kWh
