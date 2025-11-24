try:
    n = int(input("enter number: "))
    if n % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
except ValueError:
    print("Please enter a valid integer.")
