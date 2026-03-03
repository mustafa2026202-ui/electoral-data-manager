import pandas as pd

def import_excel_data(file_path):
    """Imports data from an Excel file into a pandas DataFrame."""
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"An error occurred while importing the Excel file: {e}")
