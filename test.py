from firmetix import firmetix

# Create a Telemetrix object
board = firmetix.Frimetix()

piezo_pin = 3

board.set_pin_mode_digital_output(piezo_pin)

# Play a note
board.tone(piezo_pin, 440, 1000)