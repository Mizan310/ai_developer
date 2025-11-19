# RGB → Grayscale conversion (based on the given example)

def rgb_to_grayscale(image):
    grayscale_image = []   # পুরো grayscale image রাখার container
    for row in image:      # প্রতিটি row এর জন্য
        gray_row = []      # row-wise grayscale মান রাখার list
        for pixel in row:  # প্রতিটি pixel (R,G,B)
            R, G, B = pixel
            gray = round(0.299 * R + 0.587 * G + 0.114 * B)
            gray_row.append(gray)
        grayscale_image.append(gray_row)
    return grayscale_image


# Example: 3x3 RGB image (প্রতিটি pixel [123,120,115])
rgb_image = [
    [[123,120,115], [123,120,115], [123,120,115]],
    [[123,120,115], [123,120,115], [123,120,115]],
    [[123,120,115], [123,120,115], [123,120,115]]
]

gray_image = rgb_to_grayscale(rgb_image)
print(gray_image)
print("Grayscale Image:")
for row in gray_image:
    print(row)
