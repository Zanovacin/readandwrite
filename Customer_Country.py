import csv

customers = open('customers.csv','r')
csv_file = csv.reader(customers)

customer_country = open('customer_country.csv','w')


next(csv_file)


for record in csv_file:
    customer_country.write(record [1] + ',' + record[2] + ',' + record[4] + '\n')


employees = open('EmployeePay.csv','r')
csv_file2 = csv.reader(employees)




for record in csv_file2:
    print(f"First name: {record[1]} ")
    print(f"Last name: {record[2]}")
   

    