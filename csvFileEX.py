#Write
import csv

#Step 1: Write to csv file
f=open("students.csv","w",newline='')
write=csv.writer(f)

write.writerow(["Name","Marks"])
write.writerow(["Amit","85"])
write.writerow(["Riya","90"])

f.close()

#Read
#Step 2: Read from csv file
f=open("students.csv","r")
read=csv.reader(f)

for row in read:
    print(row)

f.close()