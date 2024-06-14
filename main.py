from bs4 import BeautifulSoup
import requests

# html_text = requests.get('https://www.ah.nl/bonus')
# print(html_text)


# URL of the website
url = 'https://www.ah.nl/bonus'

# Headers with a User-Agent string
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Sending a GET request with headers
response = requests.get(url, headers=headers)

# Checking the response status code
if response.status_code == 200:
    # Parsing the content
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
else:
    print(f'Failed to retrieve content, status code: {response.status_code}')