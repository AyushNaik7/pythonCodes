num1 = int(input("enter the number : "))
num2 = int(input("enter the number : "))
num3 = int(input("enter the number : "))
num4 = int(input("enter the number : "))
if (num1>num2 and num2>num3 and num3>num4):
    print("num1 is the greatest numebr")

elif (num2>num3 and num3>num4): 
    print(num2, "is the greatest number")

elif (num3>num4):
    print(num3, "is the greatest number")

else:
    print(num4, "is the greatest number")
