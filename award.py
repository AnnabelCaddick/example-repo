swim_time = float(input(" Athlete swim time (in minutes):"))
bike_time = float(input("Athlete cycle time (in minutes):"))
run_time = float(input("Athlete run time (in minutes):"))
total_triathalon_time = swim_time + bike_time + run_time
print("Well done, you completed the triathalon in" , total_triathalon_time ,  " minutes")
if 0 <= total_triathalon_time < 101:
   print(" Congratulations, you have achieved the qualifying time and will be awarded the Provincial Colours!")
elif 101 <= total_triathalon_time < 106: 
    print(" Congratulations, you finished within five minutes following the qualifying time and will therefore be awarded Provincial Half Colours!")
elif 106 <= total_triathalon_time < 111:
    print ("Congratulations, you have finished within ten minutes following the qualifying time and will therefore recieve a Provincial Scroll!")
else:
    print ("Well done for completing your triathalon! Unfortunately you finished more than 10 minutes off the qualifying time and therefore will not recieve an award.")

