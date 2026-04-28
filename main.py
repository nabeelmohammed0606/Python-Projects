#This branch is used for the questions

#efficiency question
# formula: efficiency = distance_traveled / fuel_used
# categorize cars by highly efficient: efficiency greater than 15km/l
# moderately efficienct: 10km/l and 15km/l (inclusive)
# inefficient: efficiency less than 10km/l

distance_traveled = float(input("Enter the distance traveled in km:"))

fuel_used = float(input("Enter the amount of fuel used: "))

fuel_efficiency = (distance_traveled / fuel_used)

# used for testing:
#print(f"{fuel_efficiency}")

if fuel_efficiency > 15: print("Highly Efficient")

elif 10 <= fuel_efficiency <= 15:
        print("Moderately Efficient")

else: print("Inefficient")
