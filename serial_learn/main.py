import serial


# // 打印串口数据
# // 输出 16 进制数据
# /*FD F4 83 19 44 39 DF*/
# /*FD F4 83 19 48 39 DF*/
# /*FD F4 83 19 42 39 DF*/
# /*FD F4 83 19 41 39 DF*/
#
# /*FD F4 16 EA 04 3A DF*/
# /*FD F4 16 EA 01 3A DF*/
# /*FD F4 16 EA 08 3A DF*/
# /*FD F4 16 EA 02 3A DF*/

# 定义数据
datas = [
    b'\xfd\xf4\x83\x19\x44\x39\xdf',
    b'\xfd\xf4\x83\x19\x48\x39\xdf',
    b'\xfd\xf4\x83\x19\x42\x39\xdf',
    b'\xfd\xf4\x83\x19\x41\x39\xdf',
    b'\xfd\xf4\x16\xea\x04\x3a\xdf',
    b'\xfd\xf4\x16\xea\x01\x3a\xdf',
    b'\xfd\xf4\x16\xea\x08\x3a\xdf',
    b'\xfd\xf4\x16\xea\x02\x3a\xdf'
]
# 打开串口
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.5)

if ser.is_open:
    print('串口打开成功！')
    ser.write(b'\xfd\xf4\x83\x19\x44\x39\xdf')
else:
    print('串口打开失败！')
