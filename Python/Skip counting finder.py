#formula(no. of ___'s /first num - second num)
while True:
    #variables
    a=eval(input("What are the number of ___'s between 2 given numbers : "))
    y = a+1
    print('x __ __ __ y')
    b=eval(input("What is the value of x : "))
    c=eval(input("What is the value of y : "))
    #scripts
    if b > c:
        x = b-c
        z = x/y
        print('Your rule is - ' +str(z))
        input('')
        break
    elif c > b:
        v = c-b
        u = v/y
        print('Your rule is + '+str(u))
        input('')
        break
