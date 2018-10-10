age: int = int(input("Please insert your age: "))
if age < 18:
    print("Sorry, Access only for user over 18")
    access = False
else:
    print("Welcome")
    access = True
    
