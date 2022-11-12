"""
 Copyright (c) 2022 Nils Lahaye All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

from firmetix import firmetix
from time import sleep

# Create a Telemetrix object
board = firmetix.Frimetix()

# Defining the pin
PIEZO_PIN = 3

# Setting the pin mode
board.set_pin_mode_tone(PIEZO_PIN)

# Different frequencies to test
notes =  {0,
3817,3597,3401,3205,3030,2857,2703,2551,2404,2273,2146,2024, 
1908,1805,1701,1608,1515,1433,1351,1276,1205,1136,1073,1012, 
 956, 903, 852, 804, 759, 716, 676, 638, 602, 568, 536, 506,
 478, 451, 426, 402, 379, 358, 338, 319, 301, 284, 268, 253,
 239, 226, 213, 201, 190, 179, 169, 159, 151, 142, 134, 127 }
# Play a note
for note in notes:
    board.tone(PIEZO_PIN, note, 100)
    print(note)
    sleep(0.1)
