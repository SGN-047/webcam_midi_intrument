from webcam import Webcam
from detection import Detection
import winsound
import time
import rtmidi

idiout = rtmidi.MidiOut()
# Retrieve all the open ports
available_ports = midiout.get_ports()
print(available_ports)

# Attempt to open the port
if available_ports:
    midiout.open_port(1)
else:
    midiout.open_virtual_port("My virtual output") 
# musical notes (C, D, E, F, G, A, B)
NOTES = [262, 294, 330, 350, 393, 441, 494]
NOTESmidion = [[0x90, 61, 112],[0x90, 62, 112],[0x90, 63, 112],[0x90, 64, 112],[0x90, 65, 112],[0x90, 66, 112],[0x90, 67, 112]] 
NOTESmidioff = [[0x80, 61, 0],[0x80, 62, 0],[0x80, 63, 0],[0x80, 64, 0],[0x80, 65, 0],[0x80, 66, 0],[0x80, 67, 0]]
# initialise webcam and start thread
webcam = Webcam()
webcam.start()
 
# initialise detection with first webcam frame
image = webcam.get_current_frame()
detection = Detection(image) 
 
# initialise switch
switch = True
 
while True:
 
    # get current frame from webcam
    image = webcam.get_current_frame()
     
    # use motion detection to get active cell
    cell = detection.get_active_cell(image)
    if cell == None: continue
 
    # if switch on, play note
    if switch:
        #winsound.Beep(NOTES[cell], 1000)
        #alt code
        midiout.send_message(NOTESmidion[cell])
        time.sleep(0.5)
        midiout.send_message(NOTESmidioff[cell])
     
    # alternate switch    
    switch = not switch
    del midiout
