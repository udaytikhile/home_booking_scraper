# 🏨 Booking.com Hotel Scraper (Mumbai)

This project is a Python-based web scraper that extracts hotel listings from [Booking.com](https://www.booking.com/) for Mumbai using **Selenium** (to navigate pages and save hotel cards) and **BeautifulSoup** (to parse and extract data).

---

## 🚀 Features

- Scrapes hotel **name**, **review score**, **rating number**, **price**, and **hotel link**
- Navigates through multiple pages using Selenium
- Saves listings in `.html` files
- Extracts data into a clean **CSV file** (`booking_hotels_mumbai.csv`)

---

## 🛠️ Tools & Libraries Used

- Python 3.9+
- [Selenium](https://pypi.org/project/selenium/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [pandas](https://pypi.org/project/pandas/)
- Chrome WebDriver

---

## 📂 Project Structure

booking-scraper/
│
├── data/ # Contains saved hotel card HTML files
│ ├── hotel_0.html
│ ├── hotel_1.html
│ └── ...
│
├── booking_scraper.py # Main script using Selenium
├── parser.py # Parses saved HTML files and exports CSV
├── booking_hotels_mumbai.csv # Final CSV output
├── requirements.txt # Python dependencies
└── README.md # You're reading it!


