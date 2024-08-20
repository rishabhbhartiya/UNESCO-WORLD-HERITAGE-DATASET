import pandas as pd
from bs4 import BeautifulSoup

# Function to scrape data from a local HTML file
def scrape_world_heritage_sites_from_file(file_path):
    # Open the local HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(file, 'html.parser')
    
    # Find all table rows in the tbody
    rows = soup.find('tbody').find_all('tr')
    
    # List to hold the extracted data
    heritage_sites = []

    # Loop through each row and extract data
    for row in rows:
        columns = row.find_all('td')
        
        rank = columns[0].text.strip()
        site_name = columns[1].find('a').text.strip()
        nomination_year = columns[2].find('a').text.strip()
        country = columns[3].find('a').text.strip()
        rating = columns[5].text.strip()

        # Append data to the list
        heritage_sites.append({
            'Rank': rank,
            'Site Name': site_name,
            'Nomination Year': nomination_year,
            'Country': country,
            'Rating': rating
        })
    
    return heritage_sites

# Path to the local HTML file
file_path = "/Users/rishabhbhartiya/Desktop/HERITAGE SITES/index.html"

# Scrape the data
heritage_sites = scrape_world_heritage_sites_from_file(file_path)

""" # Print the extracted data
for site in heritage_sites:
    print(site)
 """

dataset = pd.DataFrame(heritage_sites)

dataset.to_csv("WORLD HERITAGE SITES 2024 UPDATED.csv")
