system = input("Metric(M) or Imperial (I) system? ") # choosing which system

if system == "M": # selection statement for metric system
    temp = int(input("Enter temperature: ")) # temperature input
    alt = int(input("Enter altitude in metres: ")) # altitude input
    boiling_p = int(100) # boiling point at sea level
    
    # loop for subtracting 1 every 300 metres
    for i in range(alt // 300):
        boiling_p -= 1
    print("Boiling point of water at this altitude is",boiling_p,"Celsius")
    
    if temp > boiling_p: # gaseous state above the boiling point
        print("Under these conditions water is in gaseous state")
   
    elif temp <= 0: # solid state at or below 0
        print("Under these conditions water is in solid state")
  
    else: # liquid state at all other temperatures
        print("Under these conditions water is in liquid state")
        
    
elif system == "I":  # selection statement for imperial system
    temp_f = input("Enter temperature: ") # temperature input in Fahrenheit
    temp_f = float(temp_f) # making the temperature input a float
    temp = (temp_f - 32) * (5 / 9) # converting to Celsius
    print(temp_f,"Fahrenheit","=",temp,"Celsius") # printing the Celsius temperature
    alt = int(input("Enter altitude in feet: ")) # altitude input
    boiling_p = 100 # boiling point at sea level
    
    # loop for subtracting 1 every 1000 feet
    for i in range(alt // 1000):
        boiling_p -= 1
    print("Boiling point of water at this altitude is", boiling_p,"Celsius")
  
    if temp > boiling_p: # gaseous state above the boiling point
        print("Under these conditions water is in gaseous state")
    
    elif temp <= 0: # solid state at or below 0
        print("Under these conditions water is in solid state")
   
    else: # liquid state at all other temperatures
        print("Under these conditions water is in liquid state")    