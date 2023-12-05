import requests
from bs4 import BeautifulSoup

url = "https://www.meteo.gov.lk/index.php?lang=en"

try:
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    response.raise_for_status()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Define weather information classes
    weather_classes = ['last24stats']

    # Extract and print the relevant weather information
    for weather_class in weather_classes:
        weather_element = soup.find('div', {'class': weather_class})
        weather_text = getattr(weather_element, 'text', 'N/A').strip()
        print(f"{weather_text}")

        if weather_text != 'N/A':
            break  # Stop the loop if a result is found

except requests.exceptions.RequestException as e:
    print(f"Failed to retrieve data. Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
