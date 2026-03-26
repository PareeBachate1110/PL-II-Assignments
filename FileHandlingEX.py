#Step 1 : Write to File
file=open("myfile.txt","w")
file.write("Hello Students")
file.close()

#Step 2: Append to File
file=open("myfile.txt","a")
file.write("\n Welcome to Python")
file.close()

#Step 3: Read from File
file=open("myfile.txt","r")
data=file.read()
print(data)
file.close()