while True:
    try:
        num1 = eval(input("Enter a number: \n"))
        operator = input("Enter an operator(+ | / | x | -):\n")
        num2 = eval(input("Enter another number: \n"))
        if operator == '+':
            d = str(num1+num2)
            a = input("Did you mean "+ str(num1) +" + " + str(num2) + "(y/n)\n")
            if a == "y" or a == "Y":
                print("Your answer is " + d)
                c = input("Do you wish to continue?(y/n)\n")
                if c == "y" or c == "Y":
                    continue
                elif c == "n" or c == "N":
                    break
            elif a == "n" or a == "N":
                continue
            else:
                break
        elif operator == '/':
            d = str(num1/num2)
            a = input("Did you mean "+ str(num1) +" / " + str(num2) + "(y/n)\n")
            if a == "y" or a == "Y":
                print("Your answer is " + d)
                c = input("Do you wish to continue?(y/n)\n")
                if c == "y" or c == "Y":
                    continue
                elif c == "n" or c == "N":
                    break
            elif a == "n" or a == "N":
                continue
            else:
                break        
        elif operator == 'x':
            d = str(num1*num2)
            a = input("Did you mean "+ str(num1) +" x " + str(num2) + "(y/n)\n")
            if a == "y" or a == "Y":
                print("Your answer is " + d)
                c = input("Do you wish to continue?(y/n)\n")
                if c == "y" or c == "Y":
                    continue
                elif c == "n" or c == "N":
                    break
            elif a == "n" or a == "N":
                continue
            else:
                break
        elif operator == '-':
            d = str(num1-num2)
            a = input("Did you mean "+ str(num1) +" - " + str(num2) + "(y/n)\n")
            if a == "y" or a == "Y":
                print("Your answer is " + d)
                c = input("Do you wish to continue?(y/n)\n")
                if c == "y" or c == "Y":
                    continue
                elif c == "n" or c == "N":
                    break
            elif a == "n" or a == "N":
                continue
            else:
                break
        else:
            print("You need to enter one of the operators above.")

    except Exception:
        print("You need to enter a number.")