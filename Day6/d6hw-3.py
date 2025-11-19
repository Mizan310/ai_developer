# lst = [1,2,3,45,6,78]
# max = lst[0]
# for elm in lst[1:]:
#     if elm > max:
#         max = elm
# print(max)
# print(min)

image = [[100, 105, 110, 105],
        [105, 115, 120, 115],
        [110, 120, 125, 120],
        [105, 115, 120, 115]]

max = image[0][0]
min = image[0][0]
for row in image:
    for pixel in row:
        if pixel > max:
            max = pixel
        elif pixel < min:
            min = pixel
print(max)
print(min)

# min-max normalization - new_val = (old_val - min) / (max - min) * 255
for i in range(len(image)): # iterate through rows
    for j in range(len(image[i])):
        image[i][j] = (image[i][j] - min) / (max - min) * 255 # i= 0, j = 0,
print(image)
# print(image[i][j])

