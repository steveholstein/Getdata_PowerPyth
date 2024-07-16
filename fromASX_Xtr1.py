import pandas as pd


def separate_cell_values(filepath, separator=" "):
    """
    This function reads an Excel file, separates headers and values in cells,
    and writes the data to a new file, handling empty cells, missing separators,
    and numeric data.

    Args:
        filepath (str): Path to the Excel file.
        separator (str, optional): Separator between header and value (default: " ").
    """
    # Read the Excel file
    data = pd.read_excel(filepath)

    # Define a function to split based on separator and handle variations
    def split_cell(cell_value):
        try:
            # Check if cell value is a string (handles text and empty cells)
            if isinstance(cell_value, str):
                # Split based on separator (handles trailing spaces)
                parts = cell_value.rsplit(separator, 1)
                header, value = parts[0].rstrip(), parts[1]
            else:
                # Cell contains numeric data, treat it as value with empty header
                header, value = "", str(cell_value)
        except ValueError:  # No separator found
            header, value = cell_value, ""
        except IndexError:  # Empty cell
            header, value = cell_value, ""
        return header, value

    # Apply the split function to each cell in the DataFrame
    for col in data.columns:
        data[[col + "_Header", col + "_Value"]] = data[col].apply(split_cell).tolist()

    # Drop the original column with combined data
    data.drop(data.filter(like=r'^\d+$'), axis=1, inplace=True)

    # Write the separated data to a new Excel file (change filename as needed)
    data.to_excel("separated_data.xlsx", index=False)

# Example usage with different separators (modify filepath as needed)
filepath = "financial_data_2.xlsx"
separate_cell_values(filepath, separator=":")  # Colon separator
#separate_cell_values(filepath, separator="-")  # Dash separator
