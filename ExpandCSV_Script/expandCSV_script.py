import csv

input_file = 'input.csv'  # Replace with original CSV file
output_file = 'output.csv'  # expanded file

with open(input_file, newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='',
                                                                    encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)


    fieldnames = [fn for fn in reader.fieldnames if fn.lower() != 'quantity']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        try:
            qty = int(row.get('Quantity', 1))
        except ValueError:
            qty = 1

        data_row = {k: v for k, v in row.items() if k in fieldnames}
        for _ in range(qty):
            writer.writerow(data_row)

print(f"✅ Expanded data written to '{output_file}'")
