# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:41:15 2019

@author: msra2nk3
"""


#This function asks for inputs and tests to make sure they are positive integers,
#if they are not it will print a message and ask again until the input is correct


def safe_input(question):
   
    x = input(question)
    while not (x.isdigit()) or (float(x) == 0):
        print("This must be a positive integer!")
        x = input(question)
 
    return x

#Asks the user to imput parameters for the model
    
a = safe_input("How many sheep should there be?" )

b = safe_input("For how many iterations should the model run?")

c = safe_input("How large should the neighborhoods be?")

d = safe_input("How many Zombie sheep should there be?")

e = safe_input("How many landmines should there be?")

f = safe_input("How large should the landmines detection radius be?")

#Puts the inputs in the correct format to be run as a commandline entry

arguments =  "%s %s %s %s %s %s" % (a, b, c, d, e, f)

#print (arguments) #testing that the arguments have formatted correctly

print("There are", a, "sheep, ", d, "zombie sheep, and", e, "landmines remaining.") 

#runs the model with the inputted parameters

runfile("Sean_the_sheep_of_the_dead_takes_input.py", args = arguments)
