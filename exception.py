while True:
    try:
        number = int(input("Enter a number: "))
        result = number / 10
    except ValueError as e:
        print(f"Error of ValueError: {e}")
        raise ValueError("Variable not compatible")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"result: {result}")
    finally:
        print("Thank you for using")