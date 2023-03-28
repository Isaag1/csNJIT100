"""
Isaac Guerrero
CS 100 section 015
HW 01, September 9, 2021
"""

age = 20
Birth_mont = 3
Iphone_model = 12

Heght = 5.5
GPA = 3.5
Pi = 3.14

name = "Isaac"
Favorite_drink = "water"
Name_of_school = "NJIT"


mins = 42
seconds = 42
print("seconds = ", (mins * 60) + seconds)

#2.
kilometer = 10
miles = kilometer / 1.61
print("There are",("%.2f"% (miles)),"miles in 10 kilometers")

#3.
sec = 1/3600 #convert
mins = 1/60 #convert
km_to_miles = 0.62 #convert

time = (42*mins)+ (42*sec)
miles = 10 * km_to_miles

speed = miles/time # Average Speed in miles/hour

print("Average speed =", ("%.2f"% (speed)),"miles per hour")
pace = 1 #1 mile

pace_time = (pace/speed)
pace_time_min = (pace_time * 60)
pace_time_sec = (pace_time_min % 1) * 60

print("Average pace per mile =",("%d"%(pace_time_min)), "minuets and",("%.f"%(pace_time_sec)),"seconds")

#2.2
#1.
volume = ((4/3.0) * 3.14) * 5**3
print("%.2f"%(volume))
#2.
Price = 24.95
discount = .60
shippingPrice2 = .75
shippingPrice1 = 3.00
Units = 60
bookDiscountAmount = Price * discount * Units
shipping = shippingPrice2 * 59 + shippingPrice1
finalprice = bookDiscountAmount + shipping
print('The Total price is: ' ,("%.2f"%(finalprice)))

#3.
start_time = (6*60 + 52)*60
easy_time = (8*60 + 15)*2
tempo_time = (7*60 + 12)*3

breakfast = (start_time + easy_time + tempo_time)/(60*60)
breakfast_int_hour = int(breakfast)

breakfast_minute  = (breakfast - breakfast_int_hour)*60
breakfast_int_minute = int(breakfast_minute)

print('Breakfast is at ', breakfast_int_hour,".",breakfast_int_minute)
