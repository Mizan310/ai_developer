# RGB → Grayscale conversion

def rgb_to_grayscale(image):
    grayscale_image = []
    for row in image:
        gray_row = []
        for pixel in row:
            r, g, b = pixel
            gray = round(0.299 * r + 0.587 * g + 0.114 * b)
            gray_row.append(gray)
        grayscale_image.append(gray_row)
        # return gray_row
    return grayscale_image

rgb_image = [
    [[123,120,114], 
     [122,121,112], 
     [125,122,115]],

    [[123,124,114], 
     [127,122,113], 
     [125,121,112]],

    [[126,123,112], 
     [122,125,113], 
     [123,122,114]]
]

gray_image = rgb_to_grayscale(rgb_image)
print(gray_image)
row = []
for row in gray_image:
    print(row)
