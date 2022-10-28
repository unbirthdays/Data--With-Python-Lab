total = 0

open_file = open("CupcakeInvoices.csv")
for line in open_file:
    line = line.strip()
    # print(line)

    values = line.split(',')
    # print(values[2])

    quantity = float(values[3])
    price = float(values[4])
    invoice = quantity * price
    print(invoice)

    total += invoice
open_file.close()

print("TOTAL: $" + str(total))


# other way to open file
# with open("CupcakeInvoices.csv") as file:
#     df = file.read()
#     print(df)