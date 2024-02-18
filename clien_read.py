# Modbus client
from pymodbus.client import ModbusTcpClient as ModbusClient

import time

print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50210)

while True:
    time.sleep(1.0)

    # read holding registers
    rd = client.read_holding_registers(0, 10).registers
    print('Read', rd)
