#string
s="Hello" # '',"",both are same  and only single line code are writen,
# """ """ multiline codes we can write
print(type(s))
# string is immutable, we cannot change the value of string
# s[0]='h' # this will give error
# we can only change the value of string by creating a new string
#s1="  Hello World  "
# print(s1.upper()) # convert to upper case
# print(s1.lower()) # convert to lower case
# print(s1.title()) # convert to title case
# print(s1.capitalize()) # convert to capitalize case 
# print(s1.replace("Hello","Hi")) # replace the string
# print(s1.split(" ")) # split the string by space
# print(s1.split("o")) # split the string by o
# print(s1.split("l")) # split the string by l
# print(s1.casefold()) # convert to casefold(convert every char to lower case)
# print(s1.count("l")) # count the number of l in the string
# print(s1.strip()) # remove the leading and trailing spaces
# print(s1.lstrip()) # remove the leading spaces
# print(s1.rstrip()) # remove the trailing spaces
# print(s1.partition(" ")) # partition the string by space
# print(s1.startswith("Hello")) # check if the string starts with Hello
# print(s1.endswith("World")) # check if the string ends with World
# #words/methods staring with 'is' is used to check conditions
# s2="helloword"
# print(s2.isalpha()) # check if the string is alpha (only letters)
# print(s2.isalnum()) # check if the string is alphanumeric (letters and numbers)
# print(s2.isdigit()) # check if the string is digit (only numbers)
# print(s2.islower()) # check if the string is lower case
# print(s2.isupper()) # check if the string is upper case
# print(s2.encode("utf-8")) # encode the string to utf-8
# print(s2.encode("ascii")) # encode the string to ascii
# s3="Hello World"
# print(s3.zfill(20)) # fill the string with 0s to make it 20 characters long
# print(s3.rjust(20,"1")) # justify the string to the right with 1s
# print(s3.ljust(20,"2")) # justify the string to the left with 2s

#indexing give/access single char of string whereas slicing gives multiple chars of string
# s4="HelloWorld"
# print(s4.index("l")) # find the index of l in the string
# print(s4[0:5]) # slicing the string from index 0 to 5
# print(s4[-6:-1]) # slicing the string from index 6 to end
# print(s4[0:10:2]) # slicing the string from index 0 to 10 with step of 2

# age=10
# your="age is"
# print(f"your{your}age{age}")

text="My name is \"Mohit\""
print(text)
