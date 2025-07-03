#basic calculator
#defining the calculator function 
def calculator(last_result) :

    #selecting the function to perform 
    operation = input(" enter the arthemetic function you want to perform: ")

    #unvalid operational input
    if(operation != "+" and operation != "-" and operation != "*" and operation != "/"):
        #restart 
        print("unvalid operation")
        calculator(last_result)

    #next num 
    try:
        num = int(input("input second number: "))
    except:
        print("you mighthave entered wrong thing")
        calculator(last_result)

    #identify and apply the operation 
    if(operation == "+"):
        last_result += num
    elif(operation == "-"):
        last_result -= num
    elif(operation == "*"):
        last_result *= num
    elif(operation == "/"):
        last_result /= num

    #display the result 
    print(f" calculated answer: {last_result}")

    #ask for further actions
    to_continue = input(" do you want to perform another operation? yes/no ")
    if(to_continue == "yes" or to_continue == "Yes"):
        calculator(last_result)
    elif(to_continue == "no" or to_continue == "No"):
        print(f"Thanks for using the calculator. ")

    return 1

#start value
#initially before the operations the first value is also the last result 
try:
    last_result = int(input("input first number: "))
    #calling the calculator function
    calculator(last_result)
except:
    print("you mighthave entered wrong thing")
