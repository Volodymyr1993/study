import requests
from bs4 import BeautifulSoup

# URL of the page with the HTML table
url = 'view-source:https://dev.axonicportal.com/admin/casemanagement'

# Make a GET request to fetch the HTML content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table by its tag (for example <table>)
table = soup.find('table')

# Initialize a variable to store the sum
total_sum = 0

# Loop through the rows of the table
for row in table.find_all('tr'):
    # Find all cells in the row
    cells = row.find_all('td')

    # If there are cells in the row, get the data (assuming numeric data in one column)
    if cells:
        try:
            # Assuming the number is in the first column (index 0)
            value = float(cells[0].text.strip())
            total_sum += value
        except ValueError:
            # Handle rows with non-numeric values (like headers)
            pass

print(f"The total sum is: {total_sum}")
