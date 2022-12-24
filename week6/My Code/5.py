import imp
from bs4 import BeautifulSoup
with open(r"C:\Users\user\Desktop\ICT\week6\Lecture Materials\html_example.html", 'r') as file:
    content = file.read()
soup = BeautifulSoup(content)
print(soup.prettify())