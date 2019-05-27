
import random

def IsInCircle(x,y):
    if( x**2+y**2 <= 1):
        return True
    else:
        return False
    
def Find():
    error_max = 0.01
    pi_number = 3.141592
    pi_calculated = 0
    error = 3.14
    total_points = 0
    points_in_circle = 0
    
    while (error > error_max):
    #for i in range(1000):
        total_points +=1
        x = random.random()
        y = random.random()
        
        if IsInCircle(x,y):
            points_in_circle +=1
            
        pi_calculated = 4*(points_in_circle / total_points)
        error = abs(pi_number - pi_calculated)
        
    return pi_calculated , total_points


x = int(input('enter a number:'))
SumOfPI = 0


for i in range(x):
    m ,n = Find()
    print(f'number of point needed : {n}')
    print(f'pi result = {m}')
    print(f' error = {abs(3.141592 -m)}')
    SumOfPI += m
    
print(f'final result = {SumOfPI/x}')
print(f'final error = {abs(3.141592 -(SumOfPI/x))}')

        
       
        