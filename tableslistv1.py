
from bs4 import BeautifulSoup
import requests


def get_tables_and_lists(url):
    """
    This function takes a URL as input and returns a list of tables and lists found on the webpage.

    Args:
        url: The URL of the webpage to scrape.

    Returns:
        A list containing sub-lists of table data (rows and cells) and list items.
    """

    try:
        # Download the webpage content
        response = requests.get(url)
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
            if extracted_data:  # Exclude rows without data (headers only or blank ones)
                table_data.append(extracted_data)

        item_lists = []
        for list_type in lists:
            items = [item.text.strip() for item in list_type.find_all('li')]
            if items:  # Exclude empty lists (no `<li>` elements found)
                item_lists.append(items)

        return table_data, item_lists

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return [], []  # Return empty results in case of any errors

# Example usage
url = "https://finance.yahoo.com/quote/MPW/key-statistics/"  # Replace with the desired URL
tables, lists = get_tables_and_lists(url)

# Print the extracted data
if tables:
    print("Tables:")
    for table in tables:
        for row in table:
            print(row)
    print("---")

if lists:
    print("Lists:")
    for list_type in lists:
        print(list_type)
    print("---")

print("Done!")