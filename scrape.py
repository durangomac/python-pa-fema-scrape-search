import requests
from bs4 import BeautifulSoup

url = "https://www.usviodr.com/fema-pa-search-by-applicant/"

r = requests.get(url)

s = BeautifulSoup(r.content, 'html.parser')
print(s.prettify())