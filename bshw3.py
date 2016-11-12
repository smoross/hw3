print('Samantha Moross''\n''Project 3''\n''Section 002: Wednesday 5:30-6:30 pm''\n''Beautiful Soup')

print('-----------')

#B) Beautiful Soup: bshw3.py

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import requests
import re

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

student = soup.find_all(text = re.compile('student'))
for s in student: 
	txt = str(s).replace('student', 'AMAZING student') #Replace every occurance of "student" with "AMAZING student"
	s.replaceWith(txt)

for img in soup.findAll('img'):
	if img['src'] == "https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg":
		img['src'] = 'https://scontent.fdet1-2.fna.fbcdn.net/v/t1.0-9/15032822_10209747644439231_4201962823373152471_n.jpg?oh=d65072b0bd8c20647c15464e59e131ec&oe=58C88C7C'
	else: 
		img['src'] = 'media\logo.png' #Assigns every image except the one specified to the logo


pretty = str(soup)

webpage = open('file.html', 'w') #Writes to the HTML file in the directory
webpage.write(pretty)
webpage.close()







