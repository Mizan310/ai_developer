import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

if(time.strftime('%H') < '12'):
    print("Good Morning")
elif(time.strftime('%H') >= '12' and time.strftime('%H') <= '17'):
    print("Good Afternoon")
else:
    print("Goodnight")