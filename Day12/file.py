# # Opening a file for reading
# try:
#     file_object = open("my_File.txt", "r")
#     content = file_object.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     if 'file_object' in locals() and not file_object.closed:
#         file_object.close()

# # Opening a file for writing (creates or overwrites)
# with open("new_File.txt", "w") as file_object:
#     file_object.write("This is a new line.\n")
#     file_object.write("Another line.")

file_path = "E:\AI_Developer\Day12\my_File.txt"

# file = open(file_path, 'r')
# print(file.read())
# file.close()

# with open(file_path, 'r') as file:
    # print(file.read())

# with open(file_path, 'w') as file:
#     print(file.write("modified file"))

# append format
# with open(file_path, 'a') as file:
#     print(file.write("\nmodified file"))

# with open(file_path, 'w') as file:
#     print(file.write("\nmodified file"))

# with open(file_path, 'w+') as file:
#     print(file.write("\nmodified file"))
#     file.seek(0)
#     print(file.read())

with open(file_path, 'r') as file:
    # print(file.write("modified file\n"))
    # file.seek(0)
    print(file.readline())
    print(file.readline())
    print(file.readline())