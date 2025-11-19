import requests
from bs4 import BeautifulSoup

# Website to scrape (You can change this URL)
URL = "https://www.bbc.com/news"

# Fetch the page
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Extract headlines (using h2 tags)
headlines = soup.find_all("h2")

# Save to .txt file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for h in headlines:
        title = h.get_text(strip=True)
        if title:
            file.write(title + "\n")

print("✔ Headlines scraped and saved to headlines.txt")