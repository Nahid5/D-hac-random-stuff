#Nahid Sarker
#this scraper is used to get all chemical symbols and its spelling from oine website

from lxml import html
import requests

page = requests.get('http://www.lenntech.com/periodic/number/atomic-number.htm')
tree = html.fromstring(page.content)

#This will create a list of buyers:
element = tree.xpath('//strong/text()')


for x in range(len(element)):
    if ((len(element[x]) == 2 or len(element[x]) == 1 or len(element[x]) == 3)) and (("-" not in element[x]) and (" " not in element[x])):
        print("map.put(\"" + element[x].lower() + "\"" + ", " + "\"" +element[x-1] + "\");" )