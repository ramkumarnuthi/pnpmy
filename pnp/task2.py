
employee_data = {}

def add_employee():
    domain = input("Enter employee's domain: ")
    name = input("Enter employee's name: ")
    empid = input("Enter employee's empid: ")
    email = input("Enter employee's email: ")
    
    employee_info = {
        "Name": name,
        "EmpID": empid,
        "Email": email
    }
    
    if domain in employee_data:
        employee_data[domain].append(employee_info)
    else:
        employee_data[domain] = [employee_info]

def search_by_domain():
    domain = input("Enter domain to search for employees: ")
    
    if domain in employee_data:
        print(f"Employees in domain '{domain}':")
        for employee in employee_data[domain]:
            print("Name:", employee["Name"])
            print("EmpID:", employee["EmpID"])
            print("Email:", employee["Email"])
            print("-" * 20)
    else:
        print(f"No employees found in domain '{domain}'")

while True:
    print("\noptions:")
    print("1. Add Employee")
    print("2. Search Employees by Domain")
    print("3. exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        add_employee()
    elif choice == '2':
        search_by_domain()
    elif choice == '3':
        break
    else:
        print("Invalid. Please try again.")
