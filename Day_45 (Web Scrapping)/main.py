from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
web_page = response.text



soup = BeautifulSoup(web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


print(article_texts)
print(article_links)
print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])



# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "lxml")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# all_anchor_tags = soup.find_all(name="p")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)
#
# class_is_heading = soup.find_all(class_="heading")
# print(class_is_heading)
#
# h3_heading = soup.find_all(name="h3", class_="heading")
# print(h3_heading)
#
# name = soup.select_one(selector="#name")
# print(name)
