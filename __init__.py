import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath('/home/chopper/IdeaProjects/JSON/rackUpdate/enumIs.py'))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from .enumIs import Room_11_Row_1 as R1 #import file
from .enumIs import Room_11_Row_2 as R2
from .enumIs import Room_11_Row_3 as R3
from .enumIs import Room_11_Row_4 as R4


class Enums(R1, R2, R3, R4): #Multiple Inheritance
    def __init__(self, row_1, row_2, row_3, row_4):
        nameIsRow1 = "0300-PDU-FED-029-11AR16-A"
        nameIsRow2 = "0300-PDU-FED-029-11AR12-A"
        nameIsRow3 = "0300-PDU-FED-029-11AR07-A"
        nameIsRow4 = "0300-PDU-FED-029-11AR03-A"

for i in R1:
    row_1 = "0300-PDU-FED-029-11AR1{i}-A"

#print(row_1)

if __name__ =='__main__':
    print(row_1)