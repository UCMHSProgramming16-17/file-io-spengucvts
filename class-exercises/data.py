#Question to answer: What is the weight of every Generation 4 pokemon?

#import csv and requests for API
import csv
import requests
    
#Open csv file and create csv writer
file = open("pokes.csv","w")
csv = csv.writer(file,delimiter = ",")

#write to file
#id, name, weight
csv.writerow(["dex number", "name", "weight"])

#write each dex number/id in the first column
#Use for-loop to run through every Gen 4 pokemon and return the data
gen4 = range(387,494)
for id in gen4:
    
    #get the name for each dex number/id
    #Set up URL for API
    endpoint = "http://pokeapi.co/api/v2/"
    num = "pokemon/"+str(id)+"/"
    url = endpoint+num
    payload = {}
    
    #send request and check status
    r = requests.get(url, params=payload)
    print(r)
    
    #Find the name in the dictionary and set it to a variable
    dex = r.json()
    name = dex["name"]
    
    #find the weight for each pokemon and set it to a variable
    weight = dex["weight"]
    
    #write a row containing the dex number/id, name, and weight
    csv.writerow([id, name, weight])

#close file
file.close()