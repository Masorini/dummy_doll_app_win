import os
from dynamixel_sdk import *                     # Uses Dynamixel SDK library

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

# Protocol version
PROTOCOL_VERSION            = 2.0               # See which protocol version is used in the Dynamixel
BAUDRATE                    = 57600             # Dynamixel default baudrate : 57600
# Use the actual port assigned to the U2D2.
# ex) Windows: "COM*", Linux: "/dev/ttyUSB*", Mac: "/dev/tty.usbserial-*"
DEVICENAME                  = 'COM3'            # TODO: scan the com port

class DXLComInterface():
    def __init__(self):
        self.portHandler = PortHandler(DEVICENAME)
        self.packetHandler = PacketHandler(PROTOCOL_VERSION)
        pass
    
    def __open_port(self):
        if self.portHandler.openPort():
            print("Succeeded to open the port")
        else:
            print("Failed to open the port")
            print("Press any key to terminate...")
            getch()
            quit()
    
    def __set_baudrate(self):
        if self.portHandler.setBaudRate(BAUDRATE):
            print("Succeeded to change the baudrate")
        else:
            print("Failed to change the baudrate")
            print("Press any key to terminate...")
            getch()
            quit()
    
    def __close_port(self):
        self.portHandler.closePort()

    def ping(self, id):
        self.__open_port()
        self.__set_baudrate()
        dxl_model_number, dxl_comm_result, dxl_error = self.packetHandler.ping(self.portHandler, id)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))
        else:
            print("[ID:%03d] ping Succeeded. Dynamixel model number : %d" % (id, dxl_model_number))
        self.__close_port()