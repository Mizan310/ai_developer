# hw-1
def is_video_img(filename):
    # img_extensions = ".png"
    # vid_extensions = ".mp4"
    if filename.endswith(".png"):
        return "Accepted, image file"
    elif filename.endswith(".jpg"):
        return "Accepted, image file"
    elif filename.endswith(".jpeg"):
        return "Accepted, image file"
    elif filename.endswith(".mp4"):
        return "Accepted, video file"
    else:
        return "Not Accepted this file"
    
print(is_video_img("image.png"))
print(is_video_img("image.jpg"))
print(is_video_img("image.jpeg"))
print(is_video_img("video.mp4"))
print(is_video_img("document.pdf"))

# 2nd way
def validate_file(file):
    if file.endswith(".jpg"):
        print("File uploaded")
    elif file.endswith(".mp4"):
        print("File Accepted")
    else:
        print("failed")
file = input("Enter file path: ")
validate_file(file)

# 

# Practice
def calculator(x, y):  
    def sum(a, b):
        result1 = a + b
        return result1
    def sub(a, b):
        if a > b:
            result2 = a - b
            return result2
        else:
            result2 = b - a
            return result2
    a = x # or we can set another value
    b = y # or we can set another value
    sum_result = sum(a, b)
    sub_result = sub(a, b)
    return sum_result, sub_result
x = int(input("Enter First number: "))
y = int(input("Enter Second number: "))


result = calculator(x, y)
print(result)
print("Sum result: ",result[0])
print("Sub result: ", result[1])



