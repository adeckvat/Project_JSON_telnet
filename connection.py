from telnetlib import Telnet

with Telnet('10.31.65.125', 23) as tn:
    tn.interact()