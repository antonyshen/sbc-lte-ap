#!/usr/bin/python3

from __future__ import print_function
import sys
from modemcmd import modemcmd, ModemcmdTimeoutException


def main(argv):
    if len(argv) < 2:
        print('Usage: %s MODEM_DEVICE [COMMAND] [TIMEOUT]' % argv[0])
        exit(1)

    expectrsps=('OK','ERROR','SYS')
    if len(argv) > 2:
        cmd = argv[2]
    else:
        cmd = ''

    if len(argv) > 3:
        timeout = argv[3]
    else:
        timeout = 30

    print(cmd)
    try:
        print(modemcmd(argv[1], 115200, False, cmd, timeout, *expectrsps))
        exit(0)
    except ModemcmdTimeoutException as e:
        print(e)
        exit(1)
    except Exception as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main(sys.argv)
