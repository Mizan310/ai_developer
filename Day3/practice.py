user = input()
print(user)
input = user.replace(user, "good")
print(input)

split_str = "Hello World.\n I am starting python Programming"
print(split_str)
# split_sentence = split_str.split(".")
split_sentence = split_str.replace("\n", "").split(".")
print(split_sentence)
join_sentence = " ".join(split_sentence)
print(join_sentence)

# split_str2 = "Hello World.\n I am startingpython Programming"
# print(split_str2)
# mod_sentence = split_str2.replace("\n", "")
# mod_sentence = split_str2.replace(".", "")
# mod_sentence = split_str2.split()
# print(mod_sentence)
# join_sentence = " ".join(mod_sentence)
# print(join_sentence)

filename = "image.png"
is_image = filename.endswith(".png")
is_image2 = filename.startswith("image")

print("File is an image: ", is_image)
print("Fiel is an image: ", is_image2)
