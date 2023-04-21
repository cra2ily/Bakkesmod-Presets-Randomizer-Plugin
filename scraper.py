import requests
from bs4 import BeautifulSoup

# Loop through all the cars on the site and extract car codes
car_codes = []
for car_num in range(1, 3601):
    # Send an HTTP GET request to the car page for the current car number
    url = f"https://bakkesplugins.com/cars/{car_num}"
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching {url}: {e}")
        continue

    # Parse the HTML code using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the car code on the page
    code_element = soup.find('code', class_="car-code is-text-click-selectable")
    if code_element is None:
        print(f"No code found on page {url}")
        continue

    car_code = code_element.text.strip()
    print(car_code)
    # Append the car code to the list of car codes
    car_codes.append(car_code)

# Write the car codes to a file
with open('car_codes.txt', 'w') as f:
    f.write('\n'.join(car_codes))
