import csv

TAX_RATE = 0.07  # Sales tax rate

# Open the products.csv file and create a dictionary of products
products = {}
try:
    with open('products.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            products[row[0]] = {'name': row[1], 'price': float(row[2])}
except FileNotFoundError:
    print("Error: the products.csv file was not found.")
except PermissionError:
    print("Error: permission denied to open the products.csv file.")
except:
    print("Unknown error while opening the products.csv file.")

# Open the request.csv file and process the customer's order
subtotal = 0.0
items = []
try:
    with open('request.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            try:
                product = products[row[0]]
                quantity = int(row[1])
                item_total = product['price'] * quantity
                subtotal += item_total
                items.append({'name': product['name'], 'quantity': quantity, 'price': product['price'], 'total': item_total})
            except KeyError:
                print("Error: the product '{}' was not found in the catalog.".format(row[0]))
except FileNotFoundError:
    print("Error: the request.csv file was not found.")
except PermissionError:
    print("Error: permission denied to open the request.csv file.")
except:
    print("Unknown error while opening the request.csv file.")

# Print the receipt to the terminal
if items:
    print('{:<30} {:>10} {:>10} {:>10}'.format('Name', 'Quantity', 'Price', 'Total'))
    print('-' * 60)
    for item in items:
        print('{:<30} {:>10} {:>10.2f} {:>10.2f}'.format(item['name'], item['quantity'], item['price'], item['total']))
    print('-' * 60)
    tax = subtotal * TAX_RATE
    total = subtotal + tax
    print('{:>50} {:>10.2f}'.format('Subtotal:', subtotal))
    print('{:>50} {:>10.2f}'.format('Sales tax ({:.0%}):'.format(TAX_RATE), tax))
    print('{:>50} {:>10.2f}'.format('Total:', total))
else:
    print("No items found in the order.")
