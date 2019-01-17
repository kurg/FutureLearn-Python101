print("Hi, I am Kendy, your personal bot.")
UserName = input("Please enter your name : ")
print("Hello, " + UserName + ", nice to meet you.")
command = input("How can I help? ")
if command == "add":
    print("lets add some numbers")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    result = number1 + number2
    output = str(result)
    print(input1 + " + " + input2 + " = " + output)
elif command == "subtract":
    print("lets subtract some numbers")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    result = number1 - number2
    output = str(result)
    print(input1 + " - " + input2 + " = " + output)
elif command == "multiply":
    print("lets multiply some numbers")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    result = number1 * number2
    output = str(result)
    print(input1 + " x " + input2 + " = " + output)
elif command == "divide":
    print("lets divide some numbers")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    result = number1 / number2
    output = str(result)
    print(input1 + " / " + input2 + " = " + output)
else:
    print("Sorry, I don't understand.")