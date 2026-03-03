import openpyxl


def export_to_excel(data, filename):
    # Create a new workbook and select the active worksheet
    wb = openpyxl.Workbook()
    ws = wb.active

    # Write the headers to the first row
    headers = data[0].keys()
    ws.append(headers)

    # Write the data
    for row in data:
        ws.append(row.values())

    # Save the workbook to the specified filename
    wb.save(filename)
    print(f"Data exported to {filename} successfully.")
