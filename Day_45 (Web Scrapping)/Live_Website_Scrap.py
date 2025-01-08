from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text


#
soup = BeautifulSoup(web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.find(name="a").get("href")
    article_links.append(article_link)

subtexts = soup.findAll(class_="subtext")
article_upvotes = [int(line.span.span.getText().strip(" points")) if line.span.span else 0 for line in subtexts]

#
# print(article_texts)
# print(article_links)
# print(article_upvotes)
#
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
#
print(
    f"Most upvoted article: {article_texts[largest_index]}\n"
    f"Number of upvotes: {article_upvotes[largest_index]} points\n"
    f"Available at: {article_links[largest_index]}."
)

# HACKERS NEWS


