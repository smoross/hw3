print ('Project 3''\n''Samantha Moross''\n''Section 002: Wednesday 5:30-6:30 pm')

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(base_url)
html = urllib.request.urlopen(base_url).read()
soup = BeautifulSoup(r.text, 'html.parser')
print(soup)

for word in soup.find_all('student'):
	word.replace("AMAZING student", "student")

<!DOCTYPE html>





