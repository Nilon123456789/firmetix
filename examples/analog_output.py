"""
 Copyright (c) 2022 Nils Lahaye All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,f
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

 DHT support courtesy of Martyn Wheeler
 Based on the DHTNew library - https://github.com/RobTillaart/DHTNew
"""

import sys
import time

from firmetix import firmetix

"""
Setup an analog pin as an output
and toggle the pin 5 times.
"""

# Create a Frimetix instance.
board = firmetix.Firmetix()

# Analog pins number are actually following the digital pins
# So if you add the number of digital pins plus the number of the analog pin you get the actual pin number of the analog pin
# You can use the proprety called first_analog_pin to get the number of the first analog pin and you only have to add the number of the analog pin
#
# The uno has 13 digital pins and the mega has 53 digital pins
# Looking at the Uno: A0 = 14, A1 = 15, and so forth.
# Looking at a Mega2560 which has 54 digital pins: A0 = 54, A1 = 55, etc. 

# Set the pin to A1
LED_PIN = board.first_analog_pin + 1

# Set the DIGITAL_PIN as an output pin
board.set_pin_mode_digital_output(LED_PIN)

# Blink the LED and provide feedback as
# to the LED state on the console.
for blink in range(5):
    # When hitting control-c to end the program
    # in this loop, we are likely to get a KeyboardInterrupt
    # exception. Catch the exception and exit gracefully.
    try:
        print('1')
        board.digital_write(LED_PIN, 1)
        time.sleep(1)
        print('0')
        board.digital_write(LED_PIN, 0)
        time.sleep(1)
    except KeyboardInterrupt:
        board.shutdown()
        sys.exit(0)
