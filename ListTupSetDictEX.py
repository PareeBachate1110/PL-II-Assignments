select=int(input("Enter the number corresponding to the information you want to view : \n 1-Student Details, 2-Subjects, 3-Marks, 4-Result "))

#List
s=["Rahul","Shweta","Manoj","Siya"]

#Tuple
sub=("Physics","Chemistry","Maths","Biology")

#Dictionary
p_marks={
    "Rahul" : 49,
    "Shweta" : 43,
    "Manoj" : 37,
    "Siya" : 41
}

c_marks={
    "Rahul" : 50,
    "Shweta" : 39,
    "Manoj" : 37,
    "Siya" : 50
}

m_marks={
    "Rahul" : 39,
    "Shweta" : 41,
    "Manoj" : 40,
    "Siya" : 35
}

b_marks={
    "Rahul" : 45,
    "Shweta" : 34,
    "Manoj" : 37,
    "Siya" : 31
}

#Set
rahul={49,50,39,45}
shweta={43,39,41,34}
manoj={37,37,40,31}
siya={41,50,35,31}

#Menu-Based Program
if select==1:
    print("Student Details :",s)
elif select==2:
    print("Subject Details :",sub)
elif select==3:
    (print("Physics Marks :",p_marks),
    print("-------------------------------------------------------------------------"),
    print("Chemistry Marks :",c_marks),
    print("-------------------------------------------------------------------------"),
    print("Maths Marks :",m_marks),
    print("-------------------------------------------------------------------------"),
    print("Biology Marks :",b_marks),
    print("-------------------------------------------------------------------------"),
    )
elif select==4:
    (print("Rahul's Result :",rahul),
     print("--------------------------------------------------------------------"),
     print("Shweta's Result :",shweta),
     print("--------------------------------------------------------------------"),
     print("Manoj's Result :",manoj),
     print("--------------------------------------------------------------------"),
     print("Siya's Result :",siya),
     print("--------------------------------------------------------------------"),
     )
else:
    print("Please Enter a Valid Number.")
