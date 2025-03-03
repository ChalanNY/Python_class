
#Vowel

# ch=input("Enter a character:")
# if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"  or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U":
#     print(f"{ch} is an vowel")
# else:
#     print(f"{ch} is not an consonant ")

#Leap year

# yr=int(input("Enter a year:"))
# if (yr%400==0) or (yr%4==0 and yr%100!=0):
#     print(f"{yr} is a leap year")
# else:
#     print(f"{yr} is not a leap year")

#Palindrome

# st=input("Enter a string:")
# st1=st[::-1]
# if st==st1:
#     print(f"{st} is a palindrome")
# else:
#     print(f"{st} is not a palindrome")

# length and breadth

# len=int(input("Enter the length:"))
# bd=int(input("Enter the breadth:"))
# if len==bd:
#     print("The given figure is a square")
# else:
#     print("The given figure is a rectangle")

#

# gen=input("Enter the gender:")
# ht=int(input("Enter the height:"))
# if gen=="Male" or gen=="male" or gen=="M" or gen=="m":
#     if ht>=188:
#         print("He is eligible")
#     else:
#         print("He is not eligible")
# elif gen=="Female" or gen=="female" or gen=="f" or gen=="F":
#     if ht>=175:
#         print("She is eligible")
#     else:
#         print("She is not eligible")

###### while loop:

#First 50 even numbers

# x=2
# while x<=100:
#     print(x,end=" ")
#     x=x+2

#First 50 odd numbers

# x=1
# while x<=99:
#     print(x,end=" ")
#     x=x+2

#2,4,16,256,65536

# x=2
# while x<=65536:
#     print(x,end=" ")
#     x=x**2

#3125,625,125,25,5

# x=3125
# while x>=5:
#     print(x,end=" ")
#     x=x/5

#Tables:
#1

# x=1
# while x<=10:
#     print(f" 1 * {x} = {1*x}")
#     x=x+1
# print("\r")
#
# #2
#
# x=1
# while x<=10:
#     print(f" 2 * {x} = {2*x}")
#     x=x+1
# print("\r")

# for loop:

# li=[1,2,3,4]
# for i in li[::-1]:
#     print(i,end=" ")


# li=[10,20,30,40,50]
# for i in li[0:5:2]:
#     print(i,end=" ")
# print("\r")
# for i in li[3:0:-2]:
#     print(i,end=" ")

#WAP to generate the numbers from the even and odd indices separately
#WAP to generate the even and odd numbers in the list
#WAP to generate the sum of elements in the list

# li=[10,20,13,61,50]
# for x in li[0::2]:
#     print(x,end=" ")
# print("\r")
#
# for x in li[1::2]:
#     print(x,end=" ")
# print("\n")
#
# for x in li:
#     if x%2==0:
#         print(f"{x} is even")
#     else:
#         print(f"{x} is odd")
# print("\r")
#
# sum=0
# for x in li:
#     sum=sum+x
# print(f"sum is {sum}")

#WAP to print the sum of odd and even elements
#WAP to print the sum of elements present at even and odd elements

# li=[10,20,13,61,50]
# even_sum=0
# odd_sum=0
# for x in li:
#     if x %2==0:
#         even_sum+=x
#     else:
#         odd_sum+=x
# print(f"The sum of even numbers is:{even_sum}")
# print(f"The sum of odd numbers is:{odd_sum}")
# print("\r")
#
#
# evn_sum=0
# od_sum=0
# for x in li[0::2]:
#     evn_sum+=x
# for x in li[1::2]:
#     od_sum+=x
# print(f"The sum numbers at even indices are:{evn_sum}")
# print(f"The sum numbers at odd indices are:{od_sum}")

# WAP to take a string as input from the keyboard .Calculate the number of words and spaces.

# st=input("Enter a string:")
# s_count=0
# for x in st:
#     if x==" ":
#         s_count+=1
# w_count=s_count+1
# print(f"The number of words in the string is:{w_count}")
# print(f"The number of spaces in the string is:{s_count}")

# WAP to take a list of vowels.Input a character from keyboard,check whether the input character is vowel or not.

# vowels_list=["a","e","i","o","u"]
# char=input("Enter a char:").lower()
#
# for x in vowels_list:
#     if char==x:
#         print(f"The given character {char} is a vowel")
#         break
# else:
#     print(f"The given character {char} is not a vowel")

# li=[10,20,30,50,5]
# big=li[0]
# sml=li[0]
#
# for x in li:
#     if x>=big:
#         big=x
# print(f"The greatest number is:{big}")
#
# for x in li:
#     if x<=sml:
#         sml=x
# print(f" The smallest number is:{sml}")

# mydict = {}
# n = int(input("Enter how may data :"))
# for x in range(n):
#     rno = input("Enter rno :")
#     name = input("Enter name :")
#     mydict[rno]=name
# print(mydict)

#WAP to add keys and value to the empty dictionary

dict={}
dict["House number"]=int(input("Enter the House number:"))
dict["street"]=input("Enter the street:")
dict["city"]=input("Enter the city:")
dict["pincode"]=int(input("Enter the pincode:"))
print(dict)

#WAP to add elements to the empty list

# li=[]
# n=int(input("Enter the number of elements:"))
# for i in range(n):
#     ele=int(input("Enter the elements:"))
#     li.append(ele)
# print(li)

#WAP to program to check whether a number is a palindrome or not

# num=int(input('Enter a number:'))
# res=num
# rev=0
# while num>0:
#     rem=num%10
#     rev=(rev*10) + rem
#     num=num//10
# if rev==res:
#     print("palindrome")
# else:
#     print("Not a palindrome")



















