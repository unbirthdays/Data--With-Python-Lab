total_choc = 0
total_van = 0
total_sberry = 0

open_file = open("CupcakeInvoices.csv")
for line in open_file:
    line = line.strip() # gets rid of white space
    values = line.split(',') # splits by commas
    for value in values:
        if value == "Chocolate":
            total_choc += 1
        elif value == "Vanilla":
            total_van += 1
        elif value == "Strawberry":
            total_sberry += 1
    print(values[0:2]) # prints first and last names, 2 is not inclusive
open_file.close()

print(total_choc)
print(total_van)
print(total_sberry)

# with open("CupcakeInvoices.csv") as file:
#     df = file.read()
#     print(df)