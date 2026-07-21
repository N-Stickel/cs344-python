#accumulator = 0
#counter = 0
#
#while True:
#    user_input = input("Enter a number, type done to finish: ")
#
#    if user_input == "done":
#        break
#    
#    try:
#        number = float(user_input)
#        accumulator += number
#        counter += 1
#    except ValueError:
#        print("Invalid input. PLease enter a number or type done to quit.")
#
#if counter > 0:
#    average = accumulator / counter
#    print("Average of the numbers entered: ", average)
#else:
#    print("No valid numbers were entered.")
#
# Above is the original code.
# Three subtasks of this original code that could be separate functions are: 
# 1. Getting numbers in the form of user input.
# 2. Calcuting the average of the numbers entered.
# 3. Displaying the results of the average calculation.

def get_numbers():
    accumulator = 0
    counter = 0

    while True:
        user_input = input("Enter a number, type done to finish: ")

        if user_input.lower() == "done":
            break
        
        try:
            number = float(user_input)
            accumulator += number
            counter += 1
        except ValueError:
            print("Invalid input. Please enter a number or type done to quit.")

    return accumulator, counter

def calculate_average(accumulator, counter):
    if counter > 0:
        average = accumulator / counter
        return average
    else:
        return None

def display_results(average):
    if average is not None:
        print("Average of the numbers entered: ", average)
    else:
        print("No valid numbers were entered.")

def main():
    accumulator, counter = get_numbers()
    average = calculate_average(accumulator, counter)
    display_results(average)

if __name__ == "__main__":
    main()
