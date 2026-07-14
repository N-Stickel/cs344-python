accumulator = 0
counter = 0

while True:
    user_input = input("Enter a number, type done to finish: ")

    if user_input == "done":
        break
    
    try:
        number = float(user_input)
        accumulator += number
        counter += 1
    except ValueError:
        print("Invalid input. PLease enter a number or type done to quit.")

if counter > 0:
    average = accumulator / counter
    print("Average of the numbers entered: ", average)
else:
    print("No valid numbers were entered.")

