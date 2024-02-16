import math
def circle_stats(radius):
   area =  math.pi *radius ** radius
   circumference= 2* math.pi * radius
   return area, circumference
 
a,c = circle_stats(3)
print("area:",a, "Circumference:",c)
