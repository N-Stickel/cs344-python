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
        print("Record successfully added.\n")
    
def count_attendance(records, name):
    absence_count = 0

    for record in records:
        if record["name"].lower() == name.lower() and record["status"] == "A":
            absence_count += 1
        
    return absence_count

def search_attendance(records, name):
    found = False
    
    for record in records:
        if record["name"].lower() == name.lower():
            print(f"Name: {record['name']}, Date: {record['date']}, Status: {record['status']}")
            found = True
        
    if not found:
        print(f"No records found for {name}.")

def absence_alert(name, absence_count):
    print("\n ----Absence Alert---- \n")

    if absence_count >= 3:
        print(f"Alert: {name} has {absence_count} absences.")

def searching_loop(records):
    while True:
        search_input = input("Search for a name? (y/n): ").strip().lower()
        if search_input == "n":
            absence_alert(name, absence_count)
            break
        if search_input != "y":
            print("Please enter 'y' or 'n'.")
            continue
        
        name = input("Enter name to search: ").strip().lower()
        while not name:
            name = input("Please enter a name to search: ").strip().lower()
        
        search_attendance(records, name)
        absence_count = count_attendance(records, name)   

if __name__ == "__main__":
    main()
    searching_loop(attendance)
    print("\n", attendance)
