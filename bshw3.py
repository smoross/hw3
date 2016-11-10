print ('Project 3''\n''Samantha Moross''\n''Section 002: Wednesday 5:30-6:30 pm')

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import requests

base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

#Swap picture first 

words = soup.find_all('p')
for each in words:
	element = each.text
	total = re.findall('\\bstudent\\b', element)
	print (total)
	element = re.sub('\\bstudent\\b', 'AMAZING student', element)
	print (element)


txt = soup.prettify()

webpage = open('file.html', 'w') #Chapter 7 in textbook
#Write to file --> HTML code

for line in soup.find_all('a'):
	for word in line.find_all('student'):
		word.string.replace_with('AMAZING student')







