#!/usr/bin/python

# wikiScrape.py
# James Whang, 5/8/2015
# Scraper for Wikipedia

import urllib2
from bs4 import BeautifulSoup
import random
import time

nobelFile = open('nobel_preprocessed.csv').readlines()
writeFile = open('nobel_wikiScraped.csv', 'wb')
winnerNames = []
categories = ['Born', 'Nationality', 'Institutions', 'Alma mater', 'Known for', 'Notable awards']
scrapedInfo = []

for line in nobelFile:
    data = line.split(',')
    winnerNames.append(data[2])

#winnerNames = ['Marie Curie']
for winner in winnerNames:
    print winner
    newDict = {}
    winner = winner.replace(' ', '_')
    winner = winner.replace('\'', '%27')
    winner = winner.replace('\n', '')
    winner = winner.replace('"', '')
    newDict['name'] = winner

    if winner == 'Lord_Rayleigh_(John_William_Strutt)':
        winner = 'John_William_Strutt,_3rd_Baron_Rayleigh'
    
    wikipage = urllib2.urlopen(
            'http://en.wikipedia.org/wiki/' + str(winner)).read()

    soup = BeautifulSoup(wikipage)
    infoBox = soup.find('table', class_='infobox')

    #print infoBox
    if infoBox is None:
        continue
    attr_list = infoBox.find_all('th')
    attr_val_list = infoBox.find_all('td')

    index = 0

    for attr_tag in attr_list:
        attr_tag_str = str(attr_tag)
        attr = attr_tag_str.split('>')[1]
        attr = attr.split('<')[0]

        if attr in categories:
            attr_val = attr_val_list[index].get_text()
            print attr
            print attr_val
            newDict[attr] = attr_val

        index += 1
        
    time.sleep(random.random() * 5)
    scrapedInfo.append(newDict)

for item in scrapedInfo:
    for attr in item:
        writeFile.write(val.replace('\n', '').encode('utf8'))
        writeFile.write(' ') 
