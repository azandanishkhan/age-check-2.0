age_input = (input("Enter your age: "))

if not age_input.isdigit():  
    print("Error: Age must be a number without any symbols or letters!")
else:
    age = int(age_input)
    
    if age % 2 == 0:
        print(f"Your age is {age} and it is EVEN.")
    else:
        print(f"Your age is {age} and it is ODD.")
