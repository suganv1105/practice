import re

#Search the string to see if it starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
#The findall() function returns a list containing all matches.
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
#Return an empty list if no match was found:
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-e]", txt)
print(x)
#Search for the first white-space character in the string:
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
#Split at each white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
#Split the string only at the first occurrence:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
#The sub() function replaces the matches with the text of your choice:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
#Replace the first 2 occurrences:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
#Do a search that will return a Match Object:
txt = "The rain in Spain"
x = re.search("he", txt)
print(x) #this will print an object
#Print the position (start- and end-position) of the first match occurrence.
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
#Print the string passed into the function:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
#Print the part of the string where there was a match.
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())


txt = "hello world"
#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

txt = "hello world"
#Check if the string ends with 'world':
x = re.findall("world$", txt)
if x:
  print("Yes, the string ends with 'world'")
else:
  print("No match")

txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "ai" followed by 0 or more "x" characters:
x = re.findall("aix*", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "a" followed by exactly two "l" characters:
x = re.findall("al{2}", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
