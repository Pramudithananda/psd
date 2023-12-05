import requests
from bs4 import BeautifulSoup
import tkinter as tk

def fetch_weather():
    url = "https://www.meteo.gov.lk/index.php?lang=en"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        weather_classes = ['last24stats']

        for weather_class in weather_classes:
            weather_element = soup.find('div', {'class': weather_class})
            weather_text = getattr(weather_element, 'text', 'N/A').strip()
            result_label.config(text=weather_text)

            if weather_text != 'N/A':
                break
    else:
        result_label.config(text=f"Failed to retrieve data. Status code: {response.status_code}")

# Create the main window
root = tk.Tk()
root.title("Weather Information")

# Create and configure GUI components
fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.pack(pady=10)

result_label = tk.Label(root, text="", font=('Helvetica', 12))
result_label.pack(pady=10)

# Start the GUI main loop
root.mainloop()
