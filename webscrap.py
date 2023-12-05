import requests
from bs4 import BeautifulSoup

# Function to scrape headings, controlling, medicine, and food culture from a given URL
def scrape_diabetes_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract headings
    headings = [heading.text.strip() for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]

    # Extract controlling information
    controlling = soup.find('div', {'class': 'controlling-class'})
    controlling_text = controlling.text.strip() if controlling else 'Not available'

    # Extract medicine information
    medicine = soup.find('div', {'class': 'medicine-class'})
    medicine_text = medicine.text.strip() if medicine else 'Not available'

    # Extract food culture information
    food_culture = soup.find('div', {'class': 'food-culture-class'})
    food_culture_text = food_culture.text.strip() if food_culture else 'Not available'

    return headings, controlling_text, medicine_text, food_culture_text

# URLs to scrape
urls = [
    "https://www.cdc.gov/diabetes/basics/diabetes.html",
    "https://www.mayoclinic.org/diseases-conditions/diabetes/symptoms-causes/syc-20371444",
    "https://www.niddk.nih.gov/health-information/diabetes/overview/what-is-diabetes"
]

# Iterate through URLs and write results to a file
with open('diabetes_info.txt', 'w', encoding='utf-8') as file:
    for url in urls:
        headings, controlling, medicine, food_culture = scrape_diabetes_info(url)
        file.write(f"URL: {url}\n")
        file.write(f"Headings: {headings}\n")
        file.write(f"Controlling: {controlling}\n")
        file.write(f"Medicine: {medicine}\n")
        file.write(f"Food Culture: {food_culture}\n")
        file.write('\n' + '-'*50 + '\n')

print("Scraping and writing to file completed.")
