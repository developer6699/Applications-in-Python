#Estimating the pi value using Monte carlo method

import numpy as np
from numpy.random import random
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib import rcParams
    
#Running the function for certain number of iterations
def MonteCarloPi_Simulation(maxIterations):
    #Drawing a square with the help of the corner points
    square_X = [1,-1,-1,1,1]
    square_Y = [1,1,-1,-1,1]
    #Drawing a circle with the help of trignometry, cosine and sine values
    circle_X,circle_Y = [],[]
    #The total angle of circle is 2pi radians, for loop for the calculation of x an y values
    for i in range(361):
        circle_X.append(np.cos(np.pi*i/180))
        circle_Y.append(np.sin(np.pi*i/180))

    #Start keeping track of values that we need
    #Creating lists to store the respective values
    inside_X = []
    inside_Y = []
    outside_X = []
    outside_Y = []
    Iteration = []
    current_pi = []
    #Number of points that occurwithin the circle
    inside_Count = 0

    #Generate a bunch of values of x and y between -1 and 1, then assess their combined radius on an xy plane
    for i in range(maxIterations):
        #Numpy's random() function will generate a uniform random number between 0 and 1.
        #Subtracting 0.5 from random() gives a value between -0.5 and 0.5
        #Multiplying that by 2 gives a number between -1 and 1
        x = 2*(random()-0.5)
        y = 2*(random()-0.5)
        #Using pythagorous theorem to find the otherside value
        otherside = np.sqrt(x**2+y**2)
        Iteration.append(i)
        #If this otherside value is less than 1, we will add 1 to our inside_Count.
        if otherside <= 1:
            inside_Count +=1
            #Points inside the circle the circle gets added to the inside list with respect to teh x and y values
            inside_X.append(x)
            inside_Y.append(y)
        else:
            #Points inside the circle gets added to the outside list with respect to the x and y values
            outside_X.append(x)
            outside_Y.append(y)
        #Regardless whether they were inside or outside we add them to the current value of pi
        current_pi.append(4*inside_Count/(i+1))

    #Calculating the value of pi
    pi_Value = 4*inside_Count / maxIterations

    #Draw a 2D plot of where our iterations landed compared to the square and circle
    rcParams['figure.figsize'] = 5, 5
    #Plotting the square black color
    plt.plot(square_X,square_Y,color='#000000')
    #Plotting a circle with green color
    plt.plot(circle_X,circle_Y,color='#00CC00')
    #Plotting the points inside the circle with red color
    plt.scatter(inside_X,inside_Y,color='#CC0000',marker=".")
    #Plotting the points outside the circle and inside the square with blue color
    plt.scatter(outside_X,outside_Y,color='#0000CC',marker=".")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    #print out our final estimate of pi value
    print('\n' + f'Pi is approximately {pi_Value}\n')

#Give the input for the number of points
MonteCarloPi_Simulation(100)
