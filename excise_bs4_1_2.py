import requests
from bs4 import BeautifulSoup

url = "https://www.meteo.gov.lk/index.php?lang=en"

# Send a GET request to the website
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the relevant element containing the highlighted weather forecast
    forecast_summary = soup.find('p', {'dir': 'ltr', 'style': 'line-height: 1.38; text-align: justify; margin-top: 12pt; margin-bottom: 0pt;'})

    # Extract the text content of the found element
    forecast_summary_text = forecast_summary.text.strip() if forecast_summary else "N/A"

    # Print the extracted forecast summary
    print(f"Weather Forecast Summary:\n {forecast_summary_text}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
