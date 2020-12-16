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


def five_Dinamic_Equations(V1, V2, a, d, t):
    '''
    \n>> Unknow Given == 0
    \n>> Use 3 given --> Get one Unknown
    \n>> Equation1 v2 = v1 + (a * t)
    \n>> Equation2 d = (v1 + v2) / 2  * t
    \n>> Equation3 d = (v1 * t) + (0.5 * a * t**2)
    \n>> Equation4 d = (v2 * t) - (0.5 * a * t**2)
    \n>> Equation5 v2**2 = v1**1 + (2 * a * d)  
    '''
    def Equation1()