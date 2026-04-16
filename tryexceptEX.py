try:
    x=int(input("Enter Numerator : "))
    y=int(input("Enter Denominator : "))
    res=x/y
    print("Division is : ",res)

except ZeroDivisionError:
    print("Error: Cannot Divide By Zero!")

except ValueError:
    print("Please Enter A Valid Integer!")

else:
    print("Division Successful!")

finally:
    print("Code Executed Successfully!")