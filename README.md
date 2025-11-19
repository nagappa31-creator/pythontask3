Here is a clean, professional README.md for the news-headline scraper code you provided:


---

📰 News Headlines Web Scraper

This project is a simple Python script that scrapes top news headlines from a public news website (BBC News by default) and saves them into a .txt file.

It uses the requests library to fetch the webpage and BeautifulSoup to parse and extract headlines.


---

📌 Features

✔ Fetches HTML content from a news website

✔ Extracts headlines from <h2> tags

✔ Saves all collected headlines into headlines.txt

✔ Lightweight and beginner-friendly

✔ Works with any website (just change the URL)



---

🛠 Technologies Used

Python 3

requests

BeautifulSoup (bs4)


Install dependencies:

pip install requests bs4


---

📁 Project Structure

news_scraper/
│── scraper.py
│── headlines.txt
│── README.md


---

🧾 Code (scraper.py)

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


---

🚀 How to Run

1. Save the code in a file named scraper.py


2. Run the script:



python scraper.py

3. After running, a file named headlines.txt will be created containing all extracted headlines.




---

📄 Example Output (headlines.txt)

US election: Latest updates on the campaign
Global markets rise after economic data
Scientists discover new species in rainforest
Sports championship finals this weekend

(Your output will vary based on the website's current news.)


---

🔄 Customization

You can scrape any website by changing this line:

URL = "https://www.bbc.com/news"

You may also modify the tag you want to extract:

headlines = soup.find_all("h1")
# or h3, title, p, etc.


---

⚠ Important Notes

Scraper is for educational purposes only

Do not scrape sites that block bots or require login

Website structure may change, requiring code updates



---

✅ Outcome

After completing this project, you can now:

Fetch webpages using Python

Parse and extract data using BeautifulSoup

Automate the process of collecting headlines



---
