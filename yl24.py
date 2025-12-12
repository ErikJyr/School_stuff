def upc():
    number = input("Enter a UPC code: ")
    a = sum(int(number[i]) for i in range(0, 11, 2)) * 3
    b = sum(int(number[i]) for i in range(1, 11, 2))
    check = (a + b) % 10
    check_digit = 0 if check == 0 else 10 - check
    print(check_digit)

upc()


#i hate math
