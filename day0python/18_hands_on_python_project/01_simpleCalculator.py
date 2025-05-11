a =int(input("Enter the first number:"))

b = int(input("Enter the second number:"))
print("what kind of operation do you want to perform. Press + for addition\n press - for subtraction \n press * for multiplication \n press / for division")
o = input("Enter operation:")
match 0:
    case "+":
        print(f"The result is : {a+b}")
        
    case "-":
        print(f"The result is : {a-b}")

    case "*":
        print("The result is : {a*b}")    

    case "/":
        print(f"The result is : {a/b}")    
    case default:       
        print(f"something went wrong")
