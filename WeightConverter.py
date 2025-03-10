while True:
    # Get valid weight input
    while True:
        try:
            weight = float(input("Enter your weight please: "))
            break  # Exit the weight input loop if successful
        except ValueError:
            print("Please enter a numeric value for weight, not text.")
    
    # Get valid unit input
    valid_unit = False
    while not valid_unit:
        unit = input("Kilograms or Pounds (K or L): ")
        
        if unit.upper() == "K":
            weight *= 2.205
            unit = "Lbs"
            print(f"Your weight is: {round(weight,1)} {unit}")
            valid_unit = True
        elif unit.upper() == "L":
            weight /= 2.205
            unit = "Kgs"
            print(f"Your weight is: {round(weight,1)} {unit}")
            valid_unit = True
        else:
            print(f"{unit} is not valid. Please enter K or L.")
    
    # Ask if user wants to continue
    continue_program = input("Do you want to convert another weight? (yes/no): ")
    if continue_program.lower() != "yes":
        break

print("Thank you for using yazan's weight converter!")