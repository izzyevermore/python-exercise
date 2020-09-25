annual_salary = int(input("Please enter annual salary: "))
dept_code = str(input("Please enter department code: "))

if dept_code == "A":
    print("Percentage increase == 0.072") # Percentage increase
elif dept_code == "B":
    print("Percentage increase == 0.068") # Percentage increase
elif dept_code == "others":
    print("Percentage increase == 0.063") # Percentage increase

percentage_increase = float(input("Please enter percentage increase: "))

monthly_salary = (annual_salary / 12) # Before increase
print("Monthly Salary before increase ",monthly_salary)

net_monthly_salary = monthly_salary + (monthly_salary * percentage_increase)
print(net_monthly_salary)

