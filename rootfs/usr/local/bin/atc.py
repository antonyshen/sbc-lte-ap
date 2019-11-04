#! /usr/bin/env python3
import sys

from serial import Serial


def atc(port, baudrate, rtscts, cmd, timeout, *waitingrsp):
    with Serial(port=port, baudrate=baudrate, rtscts=rtscts, timeout=float(timeout)) as ser:
        if cmd != '':
            cmd = cmd +'\r'
            cmd = cmd.encode('utf-8')
            ser.write(cmd)
        else :
            cmd = cmd.encode('utf-8')

        expectrsps = []
        if len(waitingrsp) > 0:
            for rsp in waitingrsp:
                expectrsps.append(rsp.encode('utf-8'))

        glitch = b'\x00\xff'
        lines = b''
        waiting = True
        while waiting:
            line = ser.readline()

            if cmd == b'' and glitch not in line:
                lines += line
            elif cmd not in line:
                lines += line

            if line == b'':
                waiting = False
            else:
                for rsp in expectrsps:
                    if rsp in line:
                        waiting = False
                        break

    return lines.decode('utf-8')

def main(argv):
    if len(argv) < 2:
        print('AT Command utility, by Antony Shen <antony.shen@gmail.com>')
        print('Usage: %s MODEM_DEVICE [COMMAND] [TIMEOUT]' % argv[0])
        exit(1)

    expectrsps=('OK','ERROR','SYS', 'READY')
    if len(argv) > 2:
        cmd = argv[2]
    else:
        cmd = ''

    if len(argv) > 3:
        timeout = argv[3]
    else:
        timeout = 30

    print(atc(argv[1], 115200, False, cmd, timeout, *expectrsps))
    exit(0)


if __name__ == '__main__':
    main(sys.argv)
