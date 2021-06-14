from vidcapture import Webcam
import time
from signalprocessing import Detection
import rtmidi

#Initializing virtual midi
midiout = rtmidi.MidiOut()

# Retrieve all the open ports
av_ports = midiout.get_ports()
print(av_ports)

#opening the port
if av_ports:
    midiout.open_port(1)
else:
    midiout.open_virtual_port("My virtual output") 

# musical notes (C, D, E, F, G, A, B)
#array of arrays to start midi signals with tone and velocity
NOTESmidion = [[0x90, 60, 112],[0x90, 62, 112],[0x90, 64, 112],[0x90, 65, 112],[0x90, 67, 112],[0x90, 69, 112],[0x90, 71, 112]] 

#array of arrays to stop midi signals with tone and velocity
NOTESmidioff = [[0x80, 60, 0],[0x80, 62, 0],[0x80, 64, 0],[0x80, 65, 0],[0x80, 67, 0],[0x80, 69, 0],[0x80, 71, 0]]

# initialise webcam and start thread
cam = Webcam()
cam.capture_start()
 
# initialise detection with first webcam frag
img = cam.refresh_image()
detection = Detection(img) 
 
# variable for flow control
flow_var = True
 
while True:
 
    # get current frame from webcam
    img = cam.refresh_image()
     
    # use motion detection to get active cell
    cell = detection.active_div(img)
    if cell == None: continue
 
    
    if flow_var:
        #if flow control variable on, send corresponding midi input
        midiout.send_message(NOTESmidion[cell])
        time.sleep(0.5)
        midiout.send_message(NOTESmidioff[cell])
     
    #Exitting    
    flow_var = not flow_var
    #del midiout
