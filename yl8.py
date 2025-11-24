try:
    year = int(input("Enter a positive integer year: "))
    if year <= 0:
        print("Please enter a positive integer.")
    else:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
except ValueError:
    print("Please enter a valid integer.")
