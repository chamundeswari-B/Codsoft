def calculator():
    print("Simple Calculator")

    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        operation = input("Enter choice (1/2/3/4/5): ")

        if operation == '5':
            print("Exiting calculator. Goodbye!")
            break  # Terminate the loop

        if operation in ('1', '2', '3', '4'):
            try:
                value1 = float(input("Enter first number: ").strip())
                value2 = float(input("Enter second number: ").strip())

                if operation == '1':
                    print(f"Result: {value1} + {value2} = {value1 + value2}")
                elif operation == '2':
                    print(f"Result: {value1} - {value2} = {value1 - value2}")
                elif operation == '3':
                    print(f"Result: {value1} * {value2} = {value1 * value2}")
                elif operation == '4':
                    if value2 != 0:
                        print(f"Result: {value1} / {value2} = {value1 / value2}")
                    else:
                        print("Error! Division by zero is not allowed.")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        else:
            print("Invalid choice! Please select a valid operation.")

calculator()
