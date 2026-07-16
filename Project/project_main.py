attendance = []

def main():
    while True:
        user_input = input("Add a new attendance record? (y/n): ").strip().lower()
        if user_input == "n":
            break
        if user_input != "y":
            print("Please enter 'y' or 'n'.")
            continue
        
        name = input("Enter name: ").strip()
        while not name:
            name = input("Please enter a name: ").strip()
        
        date = input("Enter date (DD/MMM/YYYY): ").strip()
        while not date:
            date = input("Please enter a date (DD/MMM/YYYY): ").strip()
        
        status = input("Enter status (P/A): ").strip().upper()
        while status not in {"P", "A"}:
            print("please enter 'P' or 'A'.")
            status = input("enter status (P/A): ").strip().upper()
        
        record = {
            "name": name,
            "date": date,
            "status": status
        }
        attendance.append(record)
        print("Record successfulyl added.\n")
    
if __name__ == "__main__":
    main()
    print("\n", attendance)
