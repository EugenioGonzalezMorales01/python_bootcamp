from bs4 import BeautifulSoup
import lxml

with open("website.html") as web_site:
    contents = web_site.read()

soup = BeautifulSoup(contents, 'html.parser')
#print(soup.title)

for tag in soup.findAll(name="a"):
    #print(tag.get("href"))
    pass
    
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.text)

#Looking for an "a" tag inside an "p" tag
company_url = soup.select_one(selector="p a")
print(company_url)

#Looking for an tag with an specific id
company_name = soup.select_one(selector="#name")
print(company_name)

#Looking for a list of tags with a particular class
headings = soup.select(selector=".heading")
print(headings)