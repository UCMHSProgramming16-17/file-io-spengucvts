#open a file
f = open("list.txt","w")

#Write the user input to the file in a numbered list
#take 10 items
for x in range(10):
    f.write(str(x+1)+"."+input('Make a list, check it twice: ')+"\n")
    
#close file
f.close()