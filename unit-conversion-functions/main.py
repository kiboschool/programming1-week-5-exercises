# Write your functions here
def km_to_miles(km):
    miles = km * 0.621371
    return round(miles, 2)

def miles_to_km(miles):
    km = miles / 0.621371
    return round(km, 2)

def lbs_to_kg(lbs):
    kg = lbs * 0.453592
    return round(kg, 2)

def kg_to_lbs(kg):
    lbs = kg / 0.453592
    return round(lbs, 2)

#print(km_to_miles(10))     
#print(miles_to_km(6.21))  
#print(lbs_to_kg(86))     
print(kg_to_lbs(86))   