from __future__ import print_function, division
from PyAstronomy import pyasl
import sys
import os

def jd_to_cd(jd):
# Convert JD to calendar date
    os.system('cls' if os.name == 'nt' else 'clear') 
    jd = float(jd)
    dt = pyasl.daycnv(jd, mode='dt')
    print("Datetime: ", dt)

jd_to_cd(sys.argv[1])