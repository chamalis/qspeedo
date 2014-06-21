#!/usr/bin/env  python

import serial   #arduino
import time     #timers
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#from PyQt4.Qwt import *   #Knob
import sys    #execution
import thread  #execute GUI as worker thread to run in parallel with arduino com/on
from string import atof

#from window import Window
from ui_speedo import Ui_Speedo

INPUT_STRING  = '9'
STOP_STRING = 's'
TERMINATION_CHAR='@'
SERIAL_PORT_FILE = '/dev/ttyACM0'
WRONG_STRING = 'w'
ROTATION_LIMIT	=	5
WRITE_TO_FILE_DELAY =	25
WHEEL_DIAMETER	=	0.55   #meters
PI	 = 3.14159 
MSEC_TO_KMH	= 3.6 


class Arduino():
 
    def __init__(self, path=SERIAL_PORT_FILE, baud=9600):
        self.ser = serial.Serial(path, baud)   
        try:
            self.ser.open()
        except serial.SerialException, e:
            logging.error("Could not open serial port %s: %s" % (path, e))
            sys.exit(1)
        time.sleep(2)
        print "Opened serial port %s. Connection Established" %path
    
    def send(self, data):
        self.ser.write(data)
 
    def read(self):
        data = ""
        while (1):
            char = self.ser.read(1)       #read 1 byte at a time
            data += char
            if char == TERMINATION_CHAR:    #reached the end of the incoming string
                return data.rstrip(TERMINATION_CHAR)   #remove termchar before returning
            elif char == STOP_STRING:           #game over
                sys.exit(0)
 
    def flush(self):
        self.ser.flushInput()
        self.ser.flushOutput()
    
    '''Attached to thread in main, executing in parallel with the widget (app) - which are
    passed as references in order to update them from here correctly '''
    def begin_communication(self, ui, app):
        
        startTime =time2 = time.time()
        lastRotations=0.0;
        velocity=0.0;
        while True:
            time1 = time.time()
            #read from arduino by giving the appropriate signal
            self.flush()   #clean buffer
            self.send(INPUT_STRING)    #send arduino appropriate signal
            data = self.read()                #read until termination char is reached
            print data      #debugging shit
            
            values = data.split('_')    #split around '_' aka: get three clean values: voltage,intensity,rotations
            voltage = atof(values[0])
            intensity = atof(values[1])
            rotations = atof(values[2])
            
            #calculate(update) velocity... also update lastRotations and time2. 
            velocity, lastRotations, time2 = self.speedoMeter(velocity, lastRotations, rotations, time1, time2)   

            #Update the GUI
            ui.lcdVoltage.display(voltage)      
            ui.lcdIntensity.display(intensity)    
            ui.lcdSpeed.display(velocity)
            ui.lcdPower.display(voltage*intensity)
            ui.lcdTime.display(time1 - startTime)   #time elapsed so far
            app.processEvents()    #else gui may stop updating ? - app is running by the main thread...
            time.sleep(0.2)   #frame refresh period (in seconds)

    def  speedoMeter(self, velocity, lastRotations, rotations, time1, time2):

        if rotations > lastRotations+ROTATION_LIMIT:
            velocity = (rotations-lastRotations) * WHEEL_DIAMETER * PI / (time1-time2)*MSEC_TO_KMH;
#            print "rotations: "+rotations+"  velocity: "+velocity
            time2 = time.time()
            lastRotations=rotations;
        return (velocity, lastRotations, time2)    #values updated at each loop iteration


''' Just a wrapper for our custom Qwidget that was created
    with QtDesigner and converted to code with pyuic4, which
    is imported at the beginning. We could add some features
    in future versions to the gui'''
class Window(QWidget):
    
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        #self.create_knob()


def main():
    
    app = QApplication(sys.argv)     #must exist since we use pyQt
    window = Window()                 #create a new window (QWidget)
    ui = Ui_Speedo()                      #create a new Ui_Speedo (our custom QWidget)
    ui.setupUi(window)                  #Ui_Speedo has ihnerited from Object so make it a proper QWidget
    window.show()
    
    ard = Arduino()
    ''' Run arduino communication in a worker thread, thus in parallel with main thread (app.exec_())
        Theoritically we should run begin_communication through QThread instead, but somehow
        native python thread works ... better :S '''
    try:
        thread.start_new_thread(ard.begin_communication, (ui,app))
    except e:
        print "Exception happened"
        print sys.exc_traceback

    #Main thread that handles the gui continues to execute in parallel with ard.begin_communication 
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
