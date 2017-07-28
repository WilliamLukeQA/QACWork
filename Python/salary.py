Salary = input("Enter Salary")
Grade = input("Enter Grade")
Dept = input("Enter Department")

salary = int(Salary)
grade = int(Grade)
dept = Dept

if salary > 15000:
    if dept == "IT":
        if grade < 11:
            tax = 9
        if grade > 10:
            tax = 15
        if grade == "CTO":
            tax = 0
        bonus = 5
    if dept == "HR":
        if grade < 11:
            tax = 9
        if grade > 10:
            tax = 17
        if grade == "CTO":
            tax = 2
    else:
        print('Please enter either "IT" or "HR"')

salary = salary + (salary/100*int(bonus))
after = salary - (salary/100*int(tax))

print("Salary after tax = %s" %after)
