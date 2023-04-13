import math
#Dividing by 10000 to scale R, r and a values
R = 6/10000
r = 1/10000
a = 8/10000
n = 16
t = 0.00

#Storing latitude and longitude values
lon = 34.020463
lat = -118.285445
pi = math.pi

while t<(n*pi):
  x = (R+r)*math.cos((r/R)*t) - a*math.cos((1+r/R)*t) + lat
  y = (R+r)*math.sin((r/R)*t) - a*math.sin((1+r/R)*t) + lon
  #Increment t in steps of 0.01
  t = t + 0.01
  #PRint resulting string
  print(str(x)+","+str(y)+","+"0.\n")
 