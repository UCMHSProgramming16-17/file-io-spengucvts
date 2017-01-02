#open a file
f = open("donow.txt","w")

#Write the user input to the file
#take 5 items
for x in range(5):
    f.write(input('Make a list, check it twice: ')+"\n")
    
#close file
f.close()