from bs4 import BeautifulSoup
import pandas as pd
import os

data = []

for file in os.listdir("data"):
    if not file.endswith(".html"):
        continue
    with open(f"data/{file}", encoding="utf-8") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, "html.parser")

    card = soup.find("div", {"data-testid": "property-card"})
    if not card:
        continue

    # Hotel Name
    title_tag = card.find("div", {"data-testid": "title"})
    hotel_name = title_tag.text.strip() if title_tag else ""

    # Review score (like "3 reviews")
    rating_tag = card.find("div", class_="fff1944c52 fb14de7f14 eaa8455879")
    rating = rating_tag.text.strip() if rating_tag else ""

    # Rating number (like 8.5)
    review_tag = card.find("div", class_="f63b14ab7a dff2e52086")
    review_text = review_tag.text.strip() if review_tag else ""

    # Price
    price_tag = card.find("span", {"data-testid": "price-and-discounted-price"})
    price = price_tag.text.strip() if price_tag else ""

    # Link
    link = ""
    link_T = card.find("div", class_="c17271c4d7")
    if link_T:
        link_tag = link_T.find("a", href=True)
        if link_tag:
            link =  link_tag['href']

    # Save to list
    data.append({
        "Hotel Name": hotel_name,
        "Rating": review_text,
        "Review": rating,
        "Price": price,
        "Link": link
    })

df = pd.DataFrame(data)
df.to_csv("booking_hotels_mumbai.csv", index=False, encoding="utf-8-sig")

print("✅ Data saved as booking_hotels_mumbai.csv")
