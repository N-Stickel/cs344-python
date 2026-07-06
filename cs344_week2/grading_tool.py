while True:
    score = input("Enter your score as a whole number (or 'stop' to quit): ")
    # I got tired of continuously restarting the program to check more scores. This will break if any letters or words are entered other than stop in all lowercase.
    # Decimals will also break the program, hence the asking for whole numbers prompt.
    if score == "stop":
        break
    
    score = int(score)
    if score > 100 or score < 0:
        print("Invalid score. Please enter a score between 0 and 100.")
    else:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        print ("Your score of", score, "earns you a grade of", grade, ".")
