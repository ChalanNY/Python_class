# def fn_pdata(name,blood_group,*disease,email="Not given"):
#     print(f"The name of the patient is:{name}")
#     print(f"Blood group of the patient is:{blood_group}")
#     for x in disease:
#         print(f"Patient is suffering from:{x}")
#     print(f"Patients Email id is:{email}")
#     print("/r")
#
# fn_pdata("Chalan","B+","fever","cold")
# fn_pdata("Mohan","B+","Gastrick")

# def fn_sdata(name,*email,**address):
#     print(f"The nam of the student is:{name}")
#     for x in email:
#         print(f"The email ids provided by student is:{x}" )
#     for i,j in address.items():
#         print(f"{i}={j}")
#     print("\r")
#
# fn_sdata("Chalan NY","c@gmail.com","cc@gmail.com",address="Hassan",house="123")
# fn_sdata("Mohan","mc@gmail.com",address="Hassan")

#List operation:

# li=[]
# for i in  range(10):
#     ele=int(input("Enter the elements:"))
#     li.append(ele)
# print(li)
# pos=int(input("Enter the position to insert:"))
# obj=int(input("Enter the object to insert:"))
# li.insert(pos,obj)
# print(li)

# dl=int(input("Enter a number to delete:"))
# if dl in li:
#     li.remove(dl)
#     print(li)
# else:
#     print(f"{dl} is not present in the list")
#
# d_pos=int(input("Enter a position to delete:"))
# if d_pos in range(len(li)):
#     li.pop(d_pos)
#     print(li)
# else:
#     print(f"{d_pos} is not available")
#
# el=int(input("Enter the element to search its position:"))
# if el in li:
#     print(li.index(el))
# else:
#     print(f"-1")


#Tuple operation:
# tu=(1,2,3,4,5)
# pos=int(input("Enter an position to search for in tuple:"))
# if pos in tu:
#     print(f"The index is:{tu.index(pos)}")
# else:
#     print(f"{pos} is nor present in the tuple")

# se=set()
# for i in range(5):
#     num=int(input("Enter the elements:"))
#     se.add(num)
# print(se)

# create an empty dictionary , later add the below values to it ,print the dictionary, later update the name by giving another name,
# Then search for a key, if it exists then remove those pairs from the dictionary

# dict={}
# dict["Name"]=input("Enter the name:")
# dict["Email"]=input("Enter the email: ")
# dict["Mobile number"]=int(input("Enter the Mobile number:"))
# dict["City"]=input("Enter the city:")
# dict["Pincode:"]=int(input("Enter the pincode:"))
# print("\r")
# print(dict)
# print("\r")
# for i,j in dict.items():
#     print(f"{i} = {j}")
# print("\r")
#
# dict["Name"]=input("Enter another name:")
# print(dict)

# s_key=input("Enter a  search key:")

# if s_key in dict.keys():
#     dict.pop(s_key)
# print(dict)
# or
# for i in dict.keys():
#     if i== s_key:
#         dict.pop(s_key)
#         break
# print(dict)

#Program to print date and time using library functions

# import datetime
# print(datetime.datetime.now())

# import calendar
# month=int(input("Enter the month:"))
# year=int(input("Enter the year:"))
# display=calendar.month(year,month)
# print(display)

#Program to find a factorial without using models:

# num=int(input("Enter a number:"))
# for i in range(1,num):
#     num*=i
# print(num)

# 1mile=1.6km
#1 farenheit=(1 celcius*9/5)+32

# Area of a triangle:

# b=int(input("Enter the breadth of the triangle: "))
# h=int(input("Enter the height of the triangle: "))
# print(f"Area of a triangle is:{0.5*b*h}")

# Miles to kms:

# miles=int(input("Enter the distance in miles:"))
# km=miles*1.6
# print(f"The distance in kilometer is: {km}")

# swap 2 variables using 3rd variable

# a=int(input("Enter the value for a :"))
# b=int(input("Enter the value for b:"))
# temp=a
# a=b
# b=temp
# print("After swapping:")
# print(f"The value of a is:{a}")
# print(f"The value of b is:{b}")

#celcius to farenheit:

# cel=int(input("Enter the value in celcius:"))
# faren=(cel * 9/5)+32
# print(f"The value of {cel} in farenheit is:{faren}")

#prog to check whether a no is pos or neg or 0:

# num=int(input("Enter a number:"))
# print(num)
# if num<0:
#     print("The given number is negative")
# elif num>0:
#     print("The given number is positive")
# else:
#     print("The given number is zero")

#mul tables

# i=1
# while i<=10:
#     j=1
#     while j<=10:
#         print(f"{i} * {j} ={i * j}")
#         j = j + 1
#     i=i+1
#     print("\r")

# Sum of numbers

# num=int(input("Enter a number:"))
# sum=num
# for i in range(1,num):
#     sum+=i
# print(f"The sum upto given number {num} is :{sum}")









