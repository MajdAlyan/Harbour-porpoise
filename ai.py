
import pandas as pd


def read_excel_file(file_path):
    """
    Reads an Excel file and returns a DataFrame.

    Parameters:
    - file_path (str): The path to the Excel file.

    Returns:
    - pd.DataFrame: The DataFrame containing the data from the Excel file.
    """
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


# Example usage:
# Replace with the actual path to your Excel file
file_path = '/home/majd/Schreibtisch/Arbeit/\
PAL_DE/DE_PAL_6879_MP_230217_train_ok.xlsx'
# Replace with the desired sheet name or index

excel_data = read_excel_file(file_path)

if excel_data is not None:
    print(excel_data.head())  # Display the first few rows of the DataFrame


def extract_information(file_path, column_name):
    """
    Reads an Excel file, extracts information about unique values in a specified column, and returns a summary.

    Parameters:
    - file_path (str): The path to the Excel file.
    - sheet_name (str or int): The sheet to read. You can provide the sheet name or index.
    - column_name (str): The name of the column for which information needs to be extracted.

    Returns:
    - dict: A dictionary containing information about unique values in the specified column.
    """
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Extract information about unique values in the specified column
        column_info = {
            'column_name': column_name,
            'unique_values': df[column_name].unique().tolist(),
            'value_counts': df[column_name].value_counts().to_dict()
        }

        return column_info
    except Exception as e:
        print(f"Error extracting information: {e}")
        return None


# Example usage:
file_path = '/home/majd/Schreibtisch/Arbeit/\
PAL_DE/DE_PAL_6879_MP_230217_train_ok.xlsx'
# Replace with the actual path to your Excel file
column_name = 'HP'

info_result = extract_information(file_path, column_name)

if info_result is not None:
    print("Column Information:")
    print(info_result)
