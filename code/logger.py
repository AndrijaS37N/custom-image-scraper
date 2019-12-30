import logging as log
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


CYAN = '\033[96m'
BLUE = '\033[94m'
FLUORESCENT = '\033[90m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
UNDERLINE = '\033[4m'

log.basicConfig(format=UNDERLINE + YELLOW + 'Level: %(levelname)s / '
                                             'Message: %(message)s / '
                                             'Function: %(funcName)s / '
                                             'Filename: %(filename)s / '
                                             'Process: %(process)d' + RESET)
