import os
from dotenv import load_dotenv
import requests
from transformers import pipeline

os.environ["TOKENIZERS_PARALLELISM"] = "false"

load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

pipe = pipeline("text-classification", model="ProsusAI/finbert")

keyword = 'airbnb'
date = '2025-10-09'

url = (
    'https://newsapi.org/v2/everything?'
    f'q={keyword}&'
    f'from={date}&'
    'sortBy=popularity&'
    f'apiKey={api_key}'
)

response = requests.get(url)

articles = dict()

try:
    articles = response.json()['articles']
except Exception as e:
    print(e)
    print(response.json())

articles = [article for article in articles if keyword.lower() in article['title'].lower() or keyword.lower() in article['description'].lower()]

total_score = 0
num_articles = 0

for i, article in enumerate(articles):
    print(f'Title: {article["title"]}')
    print(f'Url: {article["url"]}')
    print(f'Description: {article["description"]}')

    sentiment = pipe(article["content"])[0]

    print(f'Sentiment {sentiment["label"]}, Score: {sentiment["score"]}')
    print("-" * 40)

    if sentiment["label"] == "positive":
        total_score += sentiment["score"]
        num_articles += 1
    elif sentiment["label"] == "negative":
        total_score -= sentiment["score"]
        num_articles += 1

final_score = total_score / num_articles

print(
    f'Overall Sentiment: {"Positive" if final_score >= 0.15 else "Negative" if final_score <= -0.15 else "Neutral"} {final_score}'
)
