def calculate_state(list1):
    sum = 0
    count = 0
    for item in list1:
        sum = sum + item
        count = count + 1
        avg = sum / count
    print(f"total sum: {sum}, average: {avg}")

list1 = [10, 20, 30]
calculate_state(list1)