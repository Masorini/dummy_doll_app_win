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

    def com_prepare(self):
        self.__open_port()
        self.__set_baudrate()

    def com_close(self):
        self.__close_port()

    def ping(self, id: int):
        dxl_model_number, dxl_comm_result, dxl_error = self.packetHandler.ping(self.portHandler, id)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))
        else:
            print("[ID:%03d] ping Succeeded. Dynamixel model number : %d" % (id, dxl_model_number))

    def read_1_byte_tx_rx(self, id: int, addr: int):
        dxl_data, dxl_comm_result, dxl_error = self.packetHandler.read1ByteTxRx(self.portHandler, id, addr)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))
        # TODO: how to solve the error? if error occurs, what's the meaning of dxl_data?
        return dxl_data

    def write_1_byte_tx_rx(self, id: int, addr: int, data: int):
        dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, id, addr, data)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))

    def read_4_byte_tx_rx(self, id: int, addr: int):
        dxl_data, dxl_comm_result, dxl_error = self.packetHandler.read4ByteTxRx(self.portHandler, id, addr)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))
        # TODO: how to solve the error? if error occurs, what's the meaning of dxl_data?
        return dxl_data

    def write_4_byte_tx_rx(self, id: int, addr: int, data: int):
        print(data)
        dxl_comm_result, dxl_error = self.packetHandler.write4ByteTxRx(self.portHandler, id, addr, data)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))