from app.utils import fetch_html, extract_headlines
from app.rephraser import rephrase_text
from app.summarizer import summarize_text

url = input("Enter the news website URL: ")
html = fetch_html(url)
headlines = extract_headlines(html)

print("\nOriginal Headlines:")
for h in headlines:
    print("-", h)

if headlines:
    print("\nRephrased Headline:")
    print(rephrase_text(headlines[0]))

    print("\nSummarized Article:")
    print(summarize_text(html))
