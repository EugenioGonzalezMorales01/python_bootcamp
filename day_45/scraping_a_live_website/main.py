from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
web_page_html = response.text

soup = BeautifulSoup(web_page_html, "html.parser")

#Getting the complete tags
articules_tag = soup.select(selector=".titleline > a")
articles_upvote_tag = soup.select(selector=".score")

#initializing  the variables
articles_text = []
articles_link = []
articles_upvote = []

#Getting the text and link of each title tag
for tag in articules_tag:
    articles_link.append(tag.get("href"))
    articles_text.append(tag.text)
    
#Getting the score of each upvote tag
articles_upvote = [int(tag.text.split()[0]) for tag in articles_upvote_tag]
    
#Getting the highest scored title and link
highest_score_index = articles_upvote.index(max(articles_upvote))
print(articles_text[highest_score_index])
print(articles_link[highest_score_index])