from bs4 import BeautifulSoup
import requests

url='https://classroom.google.com/u/1/c/NjY2NDkxNzc1NTI1'
response=requests.get(url)
soup=BeautifulSoup(response.content, 'html.parser')
p=soup.find('p')
print(p)