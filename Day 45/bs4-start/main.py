from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)  # Get the string within the title tag
# print(soup.prettify())  # Indent the contents
# print(soup.p)  # First paragraph tag
all_anchor_tags = soup.find_all(name="a")  # Find all anchor tag and put into a list

for tag in all_anchor_tags:
    print(tag.getText())  # Get anchor tags' text
    print(tag.get("href"))  # Get href attribute

heading = soup.find(name="h1", id="name")  # Get the first instance of h1 tag with id "name"
print(heading.getText())

section_heading = soup.find(name="h3", class_="heading")  # Get the first instance of h3 tag with class "heading"
print(section_heading.getText())

company_url = soup.select_one(selector="p a")
print(company_url.get("href"))

name = soup.select_one(selector="#name")  # Get the first occurrence of element with id "name"
print(name)

headings = soup.select(selector=".heading")  # Find all elements with class "heading" as a list
print(headings)
