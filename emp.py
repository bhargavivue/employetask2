import json

# Initialize an empty JSON file if it doesn't exist
file_name = "employees.json"
try:
    with open(file_name, "x") as file:
        json.dump([], file)  # Create file with an empty list if it doesn't exist
except FileExistsError:
    pass  # If the file already exists, we skip this step

def add_employee():
    """Add an employee with details entered from the terminal."""
    # Get employee details from the user
    name = input("Enter employee name: ")
    dept = input("Enter employee department: ")
    salary = float(input("Enter employee salary: "))
    id     =input("Enter employee id:")
    # Load existing employees
    with open(file_name, "r") as file:
        employees = json.load(file)

    # Auto-generate ID based on the length of the list
    new_id = len(employees) + 1
    employee = {
        "id": new_id,
        "name": name,
        "dept": dept,
        "salary": salary
    }

    # Add the new employee
    employees.append(employee)

    # Save back to the JSON file
    with open(file_name, "w") as file:
        json.dump(employees, file, indent=4)

    print(f"Employee {name} added with ID {new_id}.")

def get_salary_by_id(emp_id):
    """Get the salary of an employee based on their ID."""
    with open(file_name, "r") as file:
        employees = json.load(file)

    # Search for the employee by ID
    for employee in employees:
        if employee["id"] == emp_id:
            return employee["salary"]
    return "Employee not found."

def get_dept_by_id(emp_id):
    """Get the department of an employee based on their ID."""
    with open(file_name, "r") as file:
        employees = json.load(file)

    # Search for the employee by ID
    for employee in employees:
        if employee["id"] == emp_id:
            return employee["dept"]
    return "Employee not found."
 
def get_name_by_id ():
    """Get the salary of an employee based on their ID."""
    with open(file_name, "r") as file:
        employees = json.load(file)

# Search for the employee by name
    for employee in employees:
        if employee["name"] == get_name_by_id:
            return employee["dept"]
    return "Employee not found."



def main():
    """Main function with a menu to interact with the program."""
    while True:
        print("\nChoose an option:")
        print("1. Add a new employee")
        print("2. enter employee name")
        print("3. Get employee salary by ID")
        print("4. Get employee department by ID")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            emp_id = int(input("Enter employee ID to get salary: "))
            print("Salary:", get_salary_by_id(emp_id))
        elif choice == "3":
            emp_id = int(input("Enter employee ID to get department: "))
            print("Department:", get_dept_by_id(emp_id))
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
