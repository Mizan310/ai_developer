def addition():
    # for i in range(5):
    n = 0
    while n<5:
        try:
            a = int(input("Number1: "))
            # n = 0 # n er man 0 kore dibo
            break
        except:
            print("Only integer value")
            n=n+1
    n = 0
    while n<5:
        try:
            b = int(input("Number2: "))
            break
        except:
            print("Only integer value")
            n += 1
    print("sum", a+b)
addition()
