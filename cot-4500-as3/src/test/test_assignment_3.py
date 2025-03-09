import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.main.assignment_3 import euler_method
from src.main.assignment_3 import rungekutta

import numpy as np

a = 0     
b = 2  
y0 = 1    
N = 10    
final_y = euler_method(a, b, y0, N)
print("Euler Method result:", final_y)


final_y_runge = rungekutta()
print("Runge-Kutta result:", "{:.15f}".format(final_y_runge))