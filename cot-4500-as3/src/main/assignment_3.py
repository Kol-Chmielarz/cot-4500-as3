import numpy as np

def euler_method(a, b, y0, N):
    h = (b - a) / N
    t_values = np.linspace(a, b, N + 1)
    y_values = np.zeros(N + 1)
    y_values[0] = y0

    for i in range(N):
        f = t_values[i] - y_values[i]**2
        y_values[i + 1] = y_values[i] + h * f

    return y_values[-1]



def rungekutta():
    a = 0      
    b = 2     
    y0 = 1    
    N = 10     
    h = (b - a) / N 
    
   
    t_values = np.linspace(a, b, N + 1)
    y_values = np.zeros(N + 1)
    y_values[0] = y0

    for i in range(N):
        t = t_values[i]
        y = y_values[i]

        k1 = h * (t - y**2)
        k2 = h * ((t + h/2) - (y + k1/2)**2)
        k3 = h * ((t + h/2) - (y + k2/2)**2)
        k4 = h * ((t + h) - (y + k3)**2)

        y_values[i + 1] = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return y_values[-1]    


