# String are immutable

a= "Mizan!!!!!, Mizan is a good boy"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.strip("!"))
print(a.replace("Mizan", "Hridoy"))
print(a.split(" ")) # convert into list

blogHeading = "introduction to js"
print(blogHeading.capitalize())

str1 = "Welcome to the center"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))

print(a.count("Mizan"))

str2 = "image.png"
print(str2.endswith(".png"))

str3 = "Welcome to the console !!!"
print(str3.endswith("to", 8, 10)) # in 8 to 10 index

str4 = "Hi's name is Dan. He is an honest man"
print(str4.find("is")) # print the index

