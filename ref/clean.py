from bs4 import BeautifulSoup

def replace_tags(string, old_tag, new_tag):
    soup = BeautifulSoup(string, "html.parser")
    for node in soup.findAll(old_tag):
        node.name = new_tag
    return soup  # or return str(soup) if you want a string.
    
with open("gloss.html") as f:
    s = f.read()
soup = BeautifulSoup(s)
for a in soup.findAll('a'):
    del a['href']

soup = replace_tags(str(soup), 'a', 'span')

with open("output1.html", "w") as file:
    file.write(str(soup))