'''
    \n>> <Help>
    \n>> In : 
    \n>> Out : 
    '''
'''
    \n>> About : 
    \n>> Step : 
    \n>> Step : 
    \n>> Step : 
    \n>> Return : 
    '''

def func1_getDistance_kinemic(v, angle):
    '''
    \n>> <Help>
    \n>> In : v (velocity) + angle
    \n>> Out : d (distance)
    '''
    '''
    \n>> About : kinemic physics 
    \n>> Step : V , angle --> Vx dirc , Vy dirc
    \n>> Step : d = ( V1 * t ) - ( 0.5 * a * t**2 ) --> t 
    \n>> Return : distance
    '''
    import math
    vx, vy = v * math.cos(math.radians(60)), v * math.sin(math.radians(60))
    t = vy / 4.9
    return vx * t  


def func2_get_V_angle_kinemic(v_min, v_max, angle_min, angle_max, distance):
    '''
    \n>> <Help>
    \n>> In : v_min , v_max (range)
    \n>> Out : v , angle
    '''
    '''
    \n>> About : kinemic physics (brute force)
    \n>> Step : v , angle --> Vx , Vy 
    \n>> Step : d = (V1 * t) - (0.5 * a * t**2) --> t 
    \n>> Return : V, angle { if int(Vx * t) == distance }
    '''
    import math
    for v in range(v_min,v_max):
        for angle in range(angle_min, angle_max):
            vx, vy = v * math.cos(math.radians(60)), v * math.sin(math.radians(60))
            t = vy / 4.9
            if int(vx * t) == distance:
                return v , angle    


def func3_get_v1_v2_a_t_d_five_kinemic_equation(v1, v2, a, t, d):
    '''
    \n>> <Help>
    \n>> In : any three of v1, v2, a, t, d
    \n>> In : type None for unknown
    \n>> Return : v1 , v2 , a , d , t
    '''
    '''
    \n>> About : five kinemic equations
    \n>> Step : if elem is None --> run value in calculate() 
    \n>> Step : else --> it's good
    \n>> Step : calculate() , four ways to get answers for each value , 
    \n>> Step : keep testing , if it fails , try another solution
    \n>> Return : five values
    \n>>
    \n>> Equation1 : v2 = v1 + (a * t)
    \n>> Equation2 : d = (v1 + v2) / 2  * t
    \n>> Equation3 : d = (v1 * t) + (0.5 * a * t**2)
    \n>> Equation4 : d = (v2 * t) - (0.5 * a * t**2)
    \n>> Equation5 : v2**2 = v1**2 + (2 * a * d)  
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

