# This program inputs a time in seconds and 
# outputs the number of minutes and seconds
    	
    	
#INPUT the time in seconds
seconds_str = input("Enter a time in seconds - whole numbers only: ")# ask for input
seconds = int(seconds_str)                                                                  #convert input to integer


#CALCULATE the minutes and seconds
minutes = seconds // 60                                                                       #Integer division
remainingSeconds = seconds % 60                                                      #get the remainder
hours = minutes // 60
real_minutes = minutes - hours * 60
#OUTPUT the minutes and seconds
if minutes == 1:
    print(seconds," seconds is ",hours,"hours,",real_minutes," minute and ",remainingSeconds," seconds");
else:
    print(seconds," seconds is ",hours,"hours,",real_minutes," minutes and ",remainingSeconds," seconds");
