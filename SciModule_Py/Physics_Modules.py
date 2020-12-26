'''
Copyright (c) 2020 github.com/MuscleBrain.
All rights reserved.

Author : Eric
'''

def _1_(q_kno):
    '''
    \n# <Help>
    \n# In : v (velocity) + angle
    \n# Out : d (distance)
    '''
    '''
    \n# About : kinemic physics 
    \n# Step : V , angle --> Vx dirc , Vy dirc
    \n# Step : d = ( V1 * t ) - ( 0.5 * a * t**2 ) --> t 
    \n# Return : distance
    '''
    v, angle = q_kno[0:2]
    def getDistance(v,angle):
        import math
        vx, vy = v * math.cos(math.radians(angle)), v * math.sin(math.radians(angle))
        t = vy / 4.9
        d = vx * t
        return d
    return getDistance(v,angle)


def _2_(q_kno):
    '''
    \n# <Help>
    \n# In : v_min , v_max (range)
    \n# Out : v , angle
    '''
    '''
    \n# About : kinemic physics (brute force)
    \n# Step : v , angle --> Vx , Vy 
    \n# Step : d = (V1 * t) - (0.5 * a * t**2) --> t 
    \n# Return : V, angle { if int(Vx * t) == distance }
    '''
    v_min, v_max, angle_min, angle_max, distance = q_kno[0,5]
    def getDistance_bruteForce(v_min, v_max, angle_min, angle_max, distance):
        import math
        for v in range(v_min,v_max):
            for angle in range(angle_min, angle_max):
                vx, vy = v * math.cos(math.radians(angle)), v * math.sin(math.radians(angle))
                t = vy / 4.9
                if int(vx * t) == distance:
                    return v , angle    
    return getDistance_bruteForce(v_min, v_max, angle_min, angle_max, distance)



def _3_(q_kno):
    v1, v2, a, t, d = q_kno[0:5]
    def fiveEquations(v1, v2, a, t, d):
        '''
        \n>> <Help>
        \n>> In : any three of v1, v2, a, t, d
        \n>> In : type None for unknown
        \n>> Return : v1 , v2 , a , d , t
        '''
        '''
        \n# About : five kinemic equations
        \n# Step : if elem is None --> run value in calculate() 
        \n# Step : else --> it's good
        \n# Step : calculate() , four ways to get answers for each value , 
        \n# Step : keep testing , if it fails , try another solution
        \n# Return : five values
        \n#
        \n# Equation1 : v2 = v1 + (a * t)
        \n# Equation2 : d = (v1 + v2) / 2  * t
        \n# Equation3 : d = (v1 * t) + (0.5 * a * t**2)
        \n# Equation4 : d = (v2 * t) - (0.5 * a * t**2)
        \n# Equation5 : v2**2 = v1**2 + (2 * a * d)  
        '''
        def calculate(elem):
            try:################################## First term
                if elem == "v1":
                    elem = v2 - a * t
                    return elem
                elif elem == "v2":
                    elem = v1 + a * t
                    return elem
                elif elem == "a":
                    elem = (v2 - v1) / t
                    return elem
                elif elem == "t":
                    elem = (v2 - v1) / a
                    return elem
                elif elem == "d":
                    elem = (v1 + v2) * 2 / t
                    return elem


            except:
                try:#################################### second term
                    if elem == "v1":
                        elem = 2*d/t-v2
                        return elem
                    elif elem == "v2":
                        elem = 2*d/t-v1
                        return elem
                    elif elem == "a":
                        elem = (d - v1*t)/(0.5*t**2)
                        return elem
                    elif elem == "t":
                        elem = (2 * d) / (v1 + v2)
                        return elem
                    elif elem == "d":
                        elem = v1 * t + 0.5 * a * t ** 2
                        return elem


                except:
                    try:###################################### third term
                        if elem == "v1":
                            elem = d/t - 0.5*a*t
                            return elem
                        elif elem == "v2":
                            elem = d/t + 0.5*a*t
                            return elem
                        elif elem == "a":
                            elem = (v2 * t - d) / (0.5 * t ** 2)
                            return elem
                        elif elem == "t":
                            elem = (- v1 + (v1 ** 2 + 2 * a * d) ** 0.5) / a
                            return elem
                        elif elem == "d":
                            elem = v2 * t - 0.5 * a * t ** 2
                            return elem


                    except:
                        try:######################################## fourth term
                            if elem == "v1":
                                elem = (v2**2 - 2*a*d) **0.5
                                return elem
                            elif elem == "v2":
                                elem = (v1**2 + 2*a*d) **0.5
                                return elem
                            elif elem == "a":
                                elem = (v2 ** 2 - v1 ** 2) / (2 * d)
                                return elem
                            elif elem == "t":
                                elem = (- v1 - (v1**2 + 2*a*d)**0.5) / a
                                return elem
                            elif elem == "d":
                                elem = (v2 ** 2 - v1 ** 2)/(2 * a)
                                return elem
                        except:
                            try:
                                if elem == "t":
                                    elem = (- v2 + (v1**2 - 2*a*d)**0.5) / a
                                    return elem
                            except:
                                try:
                                    if elem == "t":
                                        elem = (- v2 - (v1**2 - 2*a*d)**0.5) / a
                                        return elem
                                except:
                                    print("O M G !")
                                    
        
        list1 = [v1, v2, a, t, d]
        list2 = ["v1", "v2", "a", "t", "d"]
        list3 = []
        for elem in range(len(list1)):
            if list1[elem] == None:
                list3.append(calculate(list2[elem]))    
            else:
                list3.append(list1[elem])
        return f"v1 = {list3[0]}, v2 = {list3[1]}, a = {list3[2]}, t = {list3[3]}, d = {list3[4]}"
    return fiveEquations(v1, v2, a, t, d)


