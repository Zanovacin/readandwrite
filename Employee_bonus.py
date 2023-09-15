import csv


employees = open('EmployeePay.csv','r')
csv_file2 = csv.reader(employees)


next(csv_file2)

for record in csv_file2:
    print((f"First name: {record[1]}"))
    print((f"Last name: {record[2]}"))
    print(f"Salary: ${int(record)[3]:10,.2f}")

    