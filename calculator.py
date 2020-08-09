menu = str(input("Enter menu for options: "))
if menu == "menu":
      print("options: ")
      print("enter 'add' or '+' to add two number")
      print("enter 'subtract' or '-' to subtract two number")
      print("enter 'multiply' or '*' to multiply two number ")
      print("enter 'divide' or '/' to divide")
      print("enter 'quit' or 'close' to end programm")
      user_input = input(": ")
   while True:
        if user_input == "quit" or "close":
          break
        elif user_input == "add" or "+":
             num1 = float(input("Enter a number: "))
             num2 = float(input("Enter another number: "))
             result = str(num1 + num2)
             print("The answer is " + result )
        elif user_input == "subtract" or "-":
             num1 = float(input("Enter a number: "))
             num2 = float(input("Enter another number: "))
             result = str(num1 - num2)
             print("The answer is " + result)
        elif user_input == "multiply" or "*":
             num1 = float(input("Enter a number: "))
             num2 = float(input("Enter another number: "))
             result = str(num1 * num2)
             print("The answer is " + result)
        elif user_input == "divide" or "/":
             num1 = float(input("Enter a number: "))
             num2 = float(input("Enter another number: "))
             result = str(num1 / num2)
             print("The answer is " + result)
        else:
            print("Unkown input")

