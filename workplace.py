workplace = input("Enter the number of the workplace: ")
print("\n--- worker's information section -----")
first_name = input("Enter the first name: ")
second_name = input("Enter the second name: ")
last_name = input("Enter the last name: ")
#prompt the user to enter values
basic_salary = float(input("Enter the basic salary: "))
allowance = float(input("Enter the allowance: "))

print("place of work:", workplace)
print("first name:", first_name)
print("last name:", last_name)
print("basic salary:", basic_salary)

#define the user-defined function
def calculate_salary(basic_salary, allowance):
    return basic_salary + allowance
salary = calculate_salary(basic_salary, allowance)
print("Net salary:", salary)