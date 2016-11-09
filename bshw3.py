print ('Project 3''\n''Samantha Moross''\n''Section 002: Wednesday 5:30-6:30 pm')

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import requests

base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(base_url)
html = urllib.request.urlopen(base_url).read()
soup = BeautifulSoup(r.text, 'html.parser')

#Swap picture first 

txt = soup.prettify()

webpage = open('file.html', 'w') #Chapter 7 in textbook
#Write to file --> HTML code

for line in soup.find_all('a'):
	for word in line.find_all('student'):
		word.string.replace_with('AMAZING student')







