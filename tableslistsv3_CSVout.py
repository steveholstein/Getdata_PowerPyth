#The provided code snippet looks almost complete! Here's the fixed version incorporating headers and addressing minor syntax errors:


from bs4 import BeautifulSoup
import requests
import csv


def get_tables_and_lists(url):
    """
    This function takes a URL as input and returns a list of tables and lists found on the webpage.

    Args:
        url: The URL of the webpage to scrape.

    Returns:
        A list containing sub-lists of table data (rows and cells) and list items.
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

        # Find all tables and unordered/ordered lists
        tables = soup.find_all('table')
        lists = soup.find_all(['ul', 'ol'])  # Search for both unordered and ordered lists

        # Extract table data and list items
        table_data = []
        for table in tables:
            rows = table.find_all('tr')
            extracted_data = [[cell.text.strip() for cell in row.find_all('td', recursive=False)] for row in rows]
            # Only append rows with data (not empty or just headers)
            if extracted_data and any(cell for row in extracted_data for cell in row):
                table_data.append(extracted_data)

        item_lists = []
        for list_type in lists:
            items = [item.text.strip() for item in list_type.find_all('li')]
            # Only append lists with items (not empty)
            if items:
                item_lists.append(items)

        return table_data, item_lists

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return [], []  # Return empty results in case of any errors


def write_to_csv(data, filename, include_header, encod):
    """
    This function takes a list of data and writes it to a CSV file.

    Args:
        data: A list containing sub-lists of data (like tables or lists).
        filename: The desired name for the output CSV file.
    """

    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if include_header == 1:
            writer.writerow(["These are all the Tables"])
        elif include_header == 2:
            # Add check for a custom message argument (not provided here)
            # If a message argument is provided, write it as the header
            # For example: write_to_csv(data, filename, include_header=2, message="Custom Header Message")
            pass
        elif include_header == 3:
            writer.writerow(["These are all the Lines"])  # Write alternative message
        elif include_header == 4:
            writer.writerow([])  # Write a blank line

        for row in data:
            writer.writerow(row)


# Example usage
url = "https://finance.yahoo.com/quote/MPW/key-statistics/"
tables, lists = get_tables_and_lists(url)

# Prepare data (assuming tables is the data you want to export)
data_to_write1 = tables
data_to_write2 = lists

# Write data to CSV
filename = "fin_data.csv"
write_to_csv(data_to_write1, filename, include_header=1, encod='utf-8')
write_to_csv(data_to_write2, filename, include_header=3, encod='utf-8')

print(f"Data scraped and written to {filename}")
print("Done!")

