from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import requests
import re

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

words = soup.find_all('p')
for each in words:
	element = each.text
	total = re.findall('\\bstudent\\b', element)
	print (total)
	element = re.sub('\\bstudent\\b', 'AMAZING student', element)
	print (element)

txt = soup.prettify()

link = soup.find_all('img')
for img in link:
	href = img['src']
	if href == 'https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg': #image extracted from HTML
		img['src'] = 'https://scontent.fdet1-2.fna.fbcdn.net/v/t1.0-9/15032822_10209747644439231_4201962823373152471_n.jpg?oh=d65072b0bd8c20647c15464e59e131ec&oe=58C88C7C'

for img in link:
	href = img['src']
	if not href.startswith("http:"):
		print('pre', img['src'])
		img['src'] = 'https://github.com/cvanlent/SI206/blob/master/HW3-StudentCopy/media/logo.png'
		print(img['src'])


pretty = str(soup)

webpage = open('file.html', 'w') #Chapter 7 in textbook
webpage.write(pretty)
webpage.close()







