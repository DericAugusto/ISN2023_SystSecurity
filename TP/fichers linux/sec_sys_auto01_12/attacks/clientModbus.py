from pymodbus.client   import ModbusTcpClient
#py3.10 from pymodbus.client  import ModbusTcpClient
import time

import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.INFO)

MODBUS_PORT = 502

UNIT=0x01

class ClientModbus(ModbusTcpClient):
    START_BUTTON = 0
    LEVEL_SENSOR = 1
    CONTACT_SENSOR = 2
    MOTOR = 1
    NOZZLE = 2
    def __init__(self, address, port = MODBUS_PORT):
        ModbusTcpClient.__init__(self, address, port)

    def read(self,addr):
        rr = self.read_coils(addr, 1)#enlever unit=UNIT py3.10
        log.debug("%s %s",addr,rr.getBit(0))
        return rr.getBit(0)

    def write(self,addr,data):
        self.write_coil(addr,data)#enlever unit=UNIT pour py3.10


if __name__ == '__main__':
    client = ClientModbus("localhost",502)
    print("Activate Start Button")
    client.write(ClientModbus.START_BUTTON,True)
    time.sleep(1)
    print("Start Button status")
    client.read(ClientModbus.START_BUTTON)
    print("Motor Status")
    client.read(ClientModbus.MOTOR)
    print("Nozzle status")
    client.read(ClientModbus.NOZZLE)
    print("Activate Contact sensor")
    client.write(ClientModbus.CONTACT_SENSOR,True)
    time.sleep(1)
    print("Deactivate Level Sensor")
    client.write(ClientModbus.LEVEL_SENSOR,False)
    time.sleep(1)
    print("Nozzle status")
    client.read(ClientModbus.NOZZLE)
    print("Motor status")
    client.read(ClientModbus.MOTOR)
    print("Activate Level Sensor")
    client.write(ClientModbus.LEVEL_SENSOR,True)
    time.sleep(1)
    print("Deactivate contact sensor")
    client.write(ClientModbus.CONTACT_SENSOR,False)
    time.sleep(1)
    print("Nozzle Status")
    client.read(ClientModbus.NOZZLE)
    print("Motor status")
    client.read(ClientModbus.MOTOR)



