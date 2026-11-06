
# #1. DATA TYPE : It tells Python what kind of data a variable contains.

# age = 13

# print(age) # 13

# print(type(age)) #tells us the type of the age variable which is int

# # int -> Integer = ....-3 , -2 , -1 , 0.. , 1 , 2 ,3 .....
# # float-> Decimals = ......8.33 , 7.25
# # str -> Text
# # bool -> Boolean Value (True / False)

# #2 . TypeCasting : Converting one datatype to other.

# age = str(age) # "13" TypeCasting

# print(type(age))


#3.-----------Taking User Input----------------->

# grade = input("Please enter your current class  \n")

# print(type(grade)) # <class 'str'> #any input from input() is always going to be a string.

# grade = int(grade) #Typecasting 

# print(type(grade)) # <class 'int'>


#4-u---------------String Indexing-------------->

# A string is a sequnce of Characters.

name = "Aryav_Nair"
# A r y a v _ N a i r
# 0 1 2 3 4 5 6 7 8 9
#-10-9-8-7-6-5-4-3-2-1

# print(name[4])  #v
# print(name[-9]) #R

#5-------------------------> String Slicing : Slicing is used to get a part of the

#syntax : string_name(start : end : step)
#start : 0(default)
#end : length of the string (default)
#step : 1 (default)

print(name[1 : 9]) # ryav_Nai

#print(name[0:10]) # Aryav_Nair
print(name[ : ]) # Aryav_Nair

print(name[::2]) # AyvNi

# # sentence = "I_am_a_good_soccer_Player"


