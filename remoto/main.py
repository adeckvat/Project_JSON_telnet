from sqlite3 import connect
from telnetlib import Telnet

import paramiko
import connection_parametrs as paramters
#with Telnet('localhost', 23) as tn:
#    tn.interact()

stdin, stdout, stderr = paramters.client.exec_command('?')

for line in stdout:
    p = paramters.line.strip('\n')
    print(p)

paramters.client.close()