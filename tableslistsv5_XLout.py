#The provided code snippet looks almost complete! Here's the fixed version incorporating headers and addressing minor syntax errors:


from bs4 import BeautifulSoup
import requests
import openpyxl

def get_tables(url):
    """
    This function takes a URL as input and returns a list of tables found on the webpage.

    Args:
        url: The URL of the webpage to scrape.

    Returns:
        A list containing sub-lists of table data (rows and cells).
    """

    # Define headers to mimic a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0 Safari/537.36'
    }

    try:
        # Download the webpage content with headers
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all tables
        tables = soup.find_all('table')

        # Extract table data
        table_data = []
        for table in tables:
            rows = table.find_all('tr')
            extracted_data = [[cell.text.strip() for cell in row.find_all(['th', 'td'], recursive=False)] for row in rows]
            # Only append rows with data (not empty or just headers)
            if extracted_data and any(cell for row in extracted_data for cell in row):
                table_data.append(extracted_data)

        return table_data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []  # Return empty results in case of any errors

def write_to_excel(data, filename):
    """
    This function takes a list of data and writes it to an Excel file.

    Args:
        data: A list containing sub-lists of table data.
        filename: The desired name for the output Excel file.
    """
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Scraped Tables"

    for table in data:
        for row in table:
            ws.append(row)
        # Append a blank row to separate tables
        ws.append([])

    wb.save(filename)

# Example usage
url = "URL"
tables = get_tables(url)

# Write data to Excel file
filename = "fin_data.xlsx"
write_to_excel(tables, filename)

print(f"Data scraped and written to {filename}")
print("Done!")
