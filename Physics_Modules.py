import math
'''
\n>>
\n>>
\n>>
\n>>
'''

def Distance__V_angle(V, angle):
    '''
    \n>> Use Velocity, angle --> Get Vx and Vy 
    \n>> Use d = (V1 * t) - (0.5 * a * t**2) --> Get t 
    \n>> Return distance
    '''
    Vx, Vy = V * math.cos(math.radians(60)), V * math.sin(math.radians(60))
    t = Vy / 4.9
    return Vx * t  


def V_angle__Distance(V_min, V_max, angle_min, angle_max, Distance):
    '''
    \n>> Use Velocity, angle --> Get Vx and Vy 
    \n>> Use d = (V1 * t) - (0.5 * a * t**2) --> Get t 
    \n>> If distance == distance --> Return V, angle 
    '''
    for V in range(V_min,V_max):
        for angle in range(angle_min, angle_max):
            Vx, Vy = V * math.cos(math.radians(60)), V * math.sin(math.radians(60))
            t = Vy / 4.9
            if int(Vx * t) == Distance:
                return V , angle    


