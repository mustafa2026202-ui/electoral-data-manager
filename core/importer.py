import pandas as pd

class Importer:
    def __init__(self):
        self.data = None
    
    def import_from_excel(self, file_path):
        """Import voter data from Excel file"""
        try:
            self.data = pd.read_excel(file_path)
            return True, f"Successfully imported {len(self.data)} records"
        except Exception as e:
            return False, f"Error importing data: {str(e)}"
    
    def get_data(self):
        """Return the imported data"""
        return self.data
    
    def get_columns(self):
        """Return the column names from imported data"""
        if self.data is not None:
            return list(self.data.columns)
        return []