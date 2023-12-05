import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.meteo.gov.lk/index.php?lang=en"

# Send a GET request to the website
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the relevant <p> element containing the weather forecast summary
    weather_summary_tag = soup.find('p', {'dir': 'ltr', 'style': 'line-height: 1.38; text-align: justify; margin-top: 12pt; margin-bottom: 0pt;'})

    # Extract the text content of the found <p> element
    weather_summary_text = weather_summary_tag.text.strip() if weather_summary_tag else "N/A"


    # Extract the text content of the found additional element
  

    # Print the extracted forecast summary
    print(f"Weather Forecast Summary:\n {weather_summary_text}")
  

    # Write the fetched information to a CSV file
    with open('weather_forecast.csv', 'w', newline='') as csvfile:
        fieldnames = ['Weather Forecast Summary', 'Additional Information']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Weather Forecast Summary': weather_summary_text}) 
        
    print("\nData written to weather_forecast.csv")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
