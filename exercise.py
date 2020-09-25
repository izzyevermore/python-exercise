contract_type = str(input("Please enter your contract type: "))
annual_salary = int(input("Please enter your annual salary: "))
if contract_type == "permanent":
    print("income_tax = 0.295") #It is a percentage
elif contract_type == "part time":
    print("Income tax is 0.25") #It is a percentage
income_tax = float(input("Please enter your tax percentage: "))
gross_montly_salary = (annual_salary / 12)
print(gross_montly_salary)
monthly_tax_payable = (gross_montly_salary * income_tax )
print('monthly_tax_payable: ', monthly_tax_payable)
net_montly_salary = (gross_montly_salary - monthly_tax_payable)
print(net_montly_salary)








