from bs4 import BeautifulSoup

#Getting a html file in my files
with open(r"C:\Users\user\Desktop\ICT\week6\Lecture Materials\html_example.html", 'r') as file:
    content = file.read()
    
# print(content)
soup = BeautifulSoup(content)


# In[ ]:


# prettify
# print(soup.prettify())


# In[ ]:


# Going trough tags
print(soup.div.div)

