#The provided code snippet looks almost complete! Here's the fixed version incorporating headers and addressing minor syntax errors:

from bs4 import BeautifulSoup
import requests

def get_tables(url):
    """
    This function takes a URL as input and returns a list of tables found on the webpage.

    Args:
        url: The URL of the webpage to scrape.

    Returns:
        A list containing the HTML code of the table elements.
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

        # Extract table HTML code
        table_html = [str(table) for table in tables]

        return table_html

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def write_to_html(tables, filename):
    """
    This function takes a list of tables and writes them to an HTML file.

    Args:
        tables: A list of HTML table strings.
        filename: The desired name for the output HTML file.
    """
    with open(filename, 'w', encoding='utf-8', errors='replace') as htmlfile:
        htmlfile.write('<html>\n<body>\n')
        htmlfile.write('<h1>These are all the Tables</h1>\n')
        for table in tables:
            htmlfile.write(table)
            htmlfile.write('<br>\n')  # Add a line break between tables
        htmlfile.write('</body>\n</html>')

# Example usage
url = "URL"
tables = get_tables(url)

# Write tables to HTML
filename = "fin_data2.html"
write_to_html(tables, filename)

print(f"Data scraped and written to {filename}")
print("Done!")

