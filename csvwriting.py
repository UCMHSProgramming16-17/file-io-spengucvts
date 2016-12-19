#import csv
import csv
import math

#open csvfile
f = open("triangles.csv","w")

#create csvwriter
csv = csv.writer(f,delimiter = ",")

#write to file
#a, b, hypotenuse
csv.writerow(["a", "b", "hypotenuse"])
#write 1-100 in the first cell
for a in range(1,101):
    #get each possible value of b
    for b in range(a,101):
    #calculate hypotenuse
        hp = math.sqrt(a**2 + b**2)
    #write a row containing a, b
        csv.writerow([a,b,hp])

#close file
f.close()