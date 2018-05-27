from decimal import *

#Introduction
print("Program to solve physics!")
print("If you don't know the variable, just do a '?'")


#Variables
	#Number Variables
weight1 = 0
normalForce1 = 0
acceleration1 = 0
netForce1 = 0
mass1 = 0
push_pullForce1 = 0
friction = 0
coefficientOfFriction1 = 0
friction1 = 0

	#String Variables
roundingNumber = int(input("Decimals to round by: "))
mass = input("Mass = ")
weight = input("Weight = ")
normalForce = input("Normal Force = ")
netForce = input("Net Force = ")
acceleration = input("Acceleration = ")
push_pullForce = input("Push/Pull Force = ")
friction = input("Friction = ")
coefficientOfFriction = input("mu = ")

getcontext().prec = roundingNumber
def rounding(varName, decimaled):
    varName = Decimal(decimaled) / 1


for i in range(10):
     #First Equation- Solves Mass     
    if mass == "?":
        if normalForce != "?":        
            mass = float(normalForce) / 10
            mass1 = Decimal(mass) / 1
            mass = str(mass1)
        elif netForce != "?" and acceleration != "?":
            mass = float(netForce) / float(acceleration)
            mass1 = Decimal(mass) / 1
            mass = str(mass1)
        else:
            mass = "?"
      
    if weight == "?":
        if mass != "?":
            weight = float(mass) * 10
            weight1 = Decimal(weight) / 1
            weight = str(weight1)            
        elif friction != "?" and coefficientOfFriction != "?":
            weight = float(friction) / float(coefficientOfFriction)
            weight1 = Decimal(weight) / 1
            weight = str(weight1)
        else:
            weight = "?"
            

    normalForce = float(weight)
    normalForce1 = Decimal(normalForce) / 1
    normalForce = str(normalForce1)
    
        
    if netForce == "?":
        if push_pullForce != "?" and friction != "?":
            netForce = float(push_pullForce) + float(friction)
            netForce1 = Decimal(netForce) / 1
            netForce = str(netForce1)
        elif mass != "?" and acceleration != "?":
            netForce = float(mass) * float(acceleration)
            netForce1 = Decimal(netForce) / 1
            netForce = str(netForce1)
        else:
            netForce = "?"

    if friction == "?":
        if netForce != "?" and push_pullForce != "?":
            friction = float(netForce) - float(push_pullForce)
            friction1 = Decimal(friction) / 1
            friction = str(friction1)
        elif acceleration != "?" and mass != "?":
            friction = float(acceleration) * float(mass)
            friction1 = Decimal(friction) / 1
            friction = str(friction1)
        elif coefficientOfFriction != "?" and normalForce != "?":
            friction = float(coefficientOfFriction) * float(normalForce)
            friction1 = Decimal(friction) / 1
            friction = str(friction1)
        else:
            friction = "?"

    if coefficientOfFriction == "?":
        coefficientOfFriction = float(friction) / float(normalForce)
        coefficientOfFriction1 = Decimal(coefficientOfFriction) / 1
        coefficientOfFriction = str(coefficientOfFriction1)
        
    if push_pullForce == "?":
        if netForce != "?" and friction != "?":
            push_pullForce = float(netForce) + float(friction)
            push_pullForce1 = Decimal(push_pullForce) / 1
            push_pullForce = str(push_pullForce1)
        else:
            push_pullForce = "?"

if acceleration == "?":
    if netForce != "?" and mass != "?":
        acceleration = float(netForce) / float(mass)
        acceleration1 = Decimal(acceleration) / 1
        acceleration = str(acceleration1)
    else:
        acceleration = "?"
       
print("Mass = " + mass + "kg")
print("Weight = " + weight + "N")
print("Acceleration = " + acceleration + "m/s/s")
print("Normal Force = " + normalForce + "N")
print("Net Force = " + netForce + "N")
print("Push/Pull Force = "+ push_pullForce + "N")
print("Friction = " + friction + "N")
print("Coefficient of Friction = " + coefficientOfFriction)
