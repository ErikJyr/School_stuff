name = input("What is your name? ")
print(f"Hello, {name}!")
answer = input("Do you live at Saaremaa? (y/n): ").strip().lower()
if answer in ("y", "yes"):
    print("Tere kõgile saarlastele!")
    age = int(input("How old are you? "))
    if age < 18:
        print(" did you know that you aren't old enough to drive?")
    else:
        print("did you know that you are old enough to drive?")
elif answer in ("n", "no"):
    print("Hello world!")
else:
    print("Unrecognized response")
