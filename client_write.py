# Modbus client
from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
import time
import random

print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50210)
reg = 0
address = 0

k1, k2, k3, k4, k5, k6, k7 = 1, 2, 3, 4, 5, 6, 7
while True:
    # random data olustur
    x = random.randint(80, 1300)
    # print(x)

    if 0 < x < 200:
        k1, k2, k3, k4, k5, k6, k7 = 1, 0, 0, 0, 0, 0, 0
    elif 200 < x < 400:
        k1, k2, k3, k4, k5, k6, k7 = 0, 1, 0, 0, 0, 0, 0
    elif 400 < x < 600:
        k1, k2, k3, k4, k5, k6, k7 = 0, 0, 1, 0, 0, 0, 0
    elif 600 < x < 800:
        k1, k2, k3, k4, k5, k6, k7 = 0, 0, 0, 1, 0, 0, 0
    elif 800 < x < 1000:
        k1, k2, k3, k4, k5, k6, k7 = 0, 0, 0, 0, 1, 0, 0
    elif 1000 < x < 1200:
        k1, k2, k3, k4, k5, k6, k7 = 0, 0, 0, 0, 0, 1, 0
    elif 1200 < x < 1400:
        k1, k2, k3, k4, k5, k6, k7 = 0, 0, 0, 0, 0, 0, 1
    else:
        k1, k2, k3, k4, k5, k6, k7 = 0, 0, 0, 0, 0, 0, 0

    data = [k1, k2, k3, k4, k5, k6, k7]

    time.sleep(1.0)
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG,
                                   wordorder=Endian.LITTLE)
    for d in data:
        builder.add_16bit_int(int(d))
    payload = builder.build()
    result = client.write_registers(int(reg), payload, skip_encode=True, unit=int(address))

#     time.sleep(1.0)
#     # write holding registers
#     builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
#     builder.add_32bit_float(random.uniform(0, 100))
#     builder.add_32bit_float(random.uniform(0, 100))
#     builder.add_32bit_float(random.uniform(0, 100))
#     builder.add_32bit_float(random.uniform(0, 100))
#     payload = builder.build()
#     client.write_registers(0, payload, skip_encode=True)
#     print('Write', payload)


#     time.sleep(1.0)
#     # write holding registers
#     builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
#     builder.add_32bit_float(random.random())
#     builder.add_32bit_float(random.random())
#     builder.add_32bit_float(random.random())
#     builder.add_32bit_float(random.random())
#     payload = builder.to_registers()
#     print('Write', payload)
#     client.write_registers(10, payload)
