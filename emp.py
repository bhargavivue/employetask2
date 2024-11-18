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
    emp_id = max([emp["id"] for emp in employees], default=0) + 1
    print(f'emp id:{emp_id}')
    employee = {
        "id": emp_id,
        "name": name,
        "dept": dept,
        "salary": salary
    }

    # Add the new employee
    employees.append(employee)

    # Save back to the JSON file
    with open(file_name, "w") as file:
        json.dump(employees, file, indent=4)

    print(f"Employee {name} added with ID {emp_id}.")

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

def get_name_by_id(emp_id):
    """Get the department of an employee based on their ID."""
    with open(file_name, "r") as file:
        employees = json.load(file)
    
    # Search for the employee by ID
    for employee in employees:
     if employee["id"] ==emp_id:       
      return employee["name"]
    return"employee not found"
     
def view_all_employees(): 
    with open(file_name, "r") as file:
        employees = json.load(file)
    if employees:
        for employee in employees:
            print(f"ID: {employee['id']}, Name: {employee['name']}, Dept: {employee['dept']}, Salary: {employee['salary']}")
    else:
        print("No employees found.")


def search_employee():
    """Search for an employee by ID or name."""
    with open(file_name, "r") as file:
        employees = json.load(file)
        emp_name = input("Enter employee name to search: ")
        for employee in employees:
            if employee["name"] == emp_name:
                print(f"Employee found: {employee}")
                return
        print("Employee not found.")
#update depatement details
def update_employee():
    """Update an employee's department or salary."""
    emp_id=int(input("Enter employee id to update:"))
    with open(file_name,"r")as file:
      employees=json.load(file)
      for employee in employees:
         
         if employee["id"]== emp_id:
           print(f"current departement: {employee['dept']}")
           # Get new department and salary
           new_dept=input(f"Enter new department for {emp_id}:")
           new_sal=float(input(f"Enter new salary for {emp_id}:"))
           if new_dept:
         # Update department if a new one is provided
            employee["dept"]=new_dept
           if new_sal:
            employee["salary"]=new_sal 
           #Save changes back to the JSON file
           with open(file_name,"w")as file:
             json.dump(employees,file,indent=4)
             print(f"Employee ID {emp_id} updated sucessfully.")
             return
           
      print(f"employee {emp_id} not found")
         

def delete_employee():
    """Delete an employee record from the system."""
    emp_id=int(input("enter the employee id to delete:"))   
    # Load the existing employee records
    with open (file_name,"r")as file:
     employess=json.load(file)  
    for employee in employess:
      if employee["id"]==emp_id:
        employess.remove(employee)
        with open(file_name,"w")as file:
         json.dump(employess,file,indent=4)
         print(f"employee id {emp_id} deleted successfully.")
         return
    print("employee id not found.")

def filter_by_department():
    """Filter employees by a specific department."""
    # Load the existing employees
    with open(file_name, "r") as file:
     employees = json.load(file)

    # Get the department from the user
    dept = input("Enter the department to filter by: ")
    #  Filter employees by the specified department using a list comprehension
    filtered =[employee for employee in employees if employee["dept"]==dept]

    # Display results
    if filtered:
      print(f"employees under department: {dept}")
      print(f"{filtered}")
    else:
      print(f"No employees found in the '{dept}' department.")

def filter_by_salary_range():
    """Filter employees based on a salary range."""
    # Load the existing employees
    with open(file_name, "r") as file:
        employees = json.load(file)

    if not employees:
        print("No employees found.")
        return

    try:
        # Get the salary range from the user
        min_salary = float(input("Enter the minimum salary: "))
        max_salary = float(input("Enter the maximum salary: "))

        # Filter employees within the salary range
        filtered_employees = [
            emp for emp in employees if min_salary <= emp["salary"] <= max_salary
        ]

        # Display results
        if filtered_employees:
            print(f"\nEmployees with salary in the range {min_salary} - {max_salary}:")
            print(f"{filtered_employees}")
        else:
            print(f"No employees found in the salary range {min_salary} - {max_salary}.")
    except ValueError:
        print("Invalid input. Please enter valid numbers for the salary range.")

def calculate_avearge_salary_by_department():
  """Calculate and display the average salary of employees in each department."""  
  with open(file_name,"r") as file:
     employees=json.load(file)
     if not employees:
        print("no employees found.")
        return
    # Group salaries by department
     department_salaries={}     
     for employee in employees:
        dept = employee.get("dept")  # Safely get the department
        salary = employee.get("salary")  # Safely get the salary
        if dept and salary:  # Ensure dept and salary exist
            if dept not in department_salaries:
                department_salaries[dept] = []
            department_salaries[dept].append(salary)  
    # Calculate and display average salary for each department
     print("\nAverage Salary by Department:")
     for dept, salaries in department_salaries.items():
        avg_salary = sum(salaries) / len(salaries)
        print(f"Department: {dept}, Average Salary: {avg_salary:.2f}")
def main():
    """Main function with a menu to interact with the program."""
while True:
    print("\nChoose an option:")
    print("1. Add a new employee")
    print("2. Get employee dept by ID")
    print("3. Get employee salary by ID")
    print("4. Get employee name by ID")
    print("5. View all employees")
    print("6. get employee by name")  
    print("7.update employee's details:")
    print("8.delete employee,s details")
    print("9.Filter employees by specific department")   
    print("10. Filter employees by salary range")
    print("11. Calculate average salary by department")
    print("12. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
            add_employee()
       
    elif choice == "2":
            emp_id = int(input("Enter employee ID to get dept: "))
            print("deparment:", get_dept_by_id(emp_id))
        
    elif choice == "3":
            emp_id = int(input("Enter employee ID to get salary: "))
            print("Salary:", get_salary_by_id(emp_id))
        
    elif choice == "4":
            emp_id = int(input("Enter employee ID to get name: "))
            print("name:", get_name_by_id(emp_id))
        
    elif choice == "5":
            view_all_employees()
        
    elif choice == "6":
            search_employee()  # Call the new search function
        
    elif choice =="7":
            update_employee()
        
    elif choice=="8":
           delete_employee()
        
    elif choice == "9":
            filter_by_department()
        
    elif choice == "10":
            filter_by_salary_range()
        
    elif choice == "11":
            calculate_avearge_salary_by_department()
    
    elif choice == "12":
         print("Exiting program.")
         break
    else:
         print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()